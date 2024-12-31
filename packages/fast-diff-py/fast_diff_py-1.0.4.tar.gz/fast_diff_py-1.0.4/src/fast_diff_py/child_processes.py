import copy
import datetime
import logging
import multiprocessing as mp
import os
import pickle
import queue
import traceback
from logging.handlers import QueueHandler
from typing import Tuple, Callable, Dict, Optional, Union

import numpy as np

import fast_diff_py.img_processing as imgp
import fast_diff_py.utils as util
from fast_diff_py.base_process import GracefulWorker
from fast_diff_py.cache import BatchCache
from fast_diff_py.datatransfer import PreprocessArg, PreprocessResult, SecondLoopArgs, SecondLoopResults


class ChildProcess(GracefulWorker):
    logger: logging.Logger = None
    log_queue: mp.Queue = None
    timeout: int
    processing_fn: Callable[..., ...] = None

    # Queues:
    cmd_queue: mp.Queue
    res_queue: mp.Queue

    block_timeout: int = 0.01

    def __init__(self, identifier: int,
                 cmd_queue: mp.Queue,
                 res_queue: mp.Queue,
                 log_queue: mp.Queue,
                 log_level: int = logging.DEBUG,
                 timeout: int = 30):

        super().__init__(identifier)
        self.timeout = timeout
        self.cmd_queue = cmd_queue
        self.res_queue = res_queue
        self.prep_logging(level=log_level, q=log_queue)

        self.fetch_arg = 0
        self.put_res = 0

    def main(self):
        """
        Main function to run the child process
        """
        # INFO: Registering interrupts leads to a dead lock when exiting. So only have the main process
        #  intercept the interrupt
        # self.register_interrupts()
        self.set_processing_function()

        count = 0
        while count < self.timeout and self.run:
            try:
                s = datetime.datetime.now(datetime.UTC)
                arg = self.cmd_queue.get(block=True, timeout=self.block_timeout)
                self.fetch_arg += (datetime.datetime.now(datetime.UTC) - s).total_seconds()
                count = 0
            except queue.Empty:
                self.logger.debug("Starving...")
                count += self.block_timeout
                continue

            # Break if we get a None
            if arg is None:
                self.res_queue.put(None)
                self.logger.info("Received None. Shutting down")
                self.logger.debug(f"{self.get_stats()}")
                return

            # Batching support via lists
            if isinstance(arg, list):
                res = []
                for a in arg:
                    res.append(self.processing_fn(a))
                self.res_queue.put(res)
            else:
                # Perform the processing
                s = datetime.datetime.now(datetime.UTC)
                self.res_queue.put(self.processing_fn(arg))
                self.put_res += (datetime.datetime.now(datetime.UTC) - s).total_seconds()

        if count >= self.timeout:
            self.logger.warning("Timeout reached. Shutting down")

        self.res_queue.put(None)
        self.logger.debug(f"{self.get_stats()}")

    def set_processing_function(self):
        """
        Set the processing function based on the configuration
        """
        raise NotImplementedError("This function needs to be implemented in the child class")

    def prep_logging(self, level: int = logging.DEBUG, q: mp.Queue = None):
        """
        Prepare the logging for the child process
        """
        self.logger = logging.getLogger(f"Child_{self.identifier:03}")
        self.logger.setLevel(level)
        self.log_queue = q

        # Need to clear the handlers
        self.logger.handlers.clear()
        q_handler = QueueHandler(q)
        self.logger.addHandler(q_handler)

    def get_stats(self):
        """
        Print timing statistics needed for debugging
        """
        return f"\nFetching Args took: {self.fetch_arg}\nPutting Results took: {self.put_res}"


class FirstLoopWorker(ChildProcess):
    processing_fn: Callable[[PreprocessArg], PreprocessResult] = None

    do_hash: bool
    compress: bool
    shift_amount: int
    thumb_dir: str
    target_size: Tuple[int, int]
    do_rot: bool

    hash_fn: Callable[[str], str] | Callable[[np.ndarray[np.uint8]], str]

    # Whether to use the old hashing method or the new one
    __old: bool = False

    def __init__(self, identifier: int,
                 cmd_queue: mp.Queue,
                 res_queue: mp.Queue,
                 log_queue: mp.Queue,

                 compress: bool,
                 do_hash: bool,
                 target_size: Tuple[int, int],
                 shift_amount: int = None,
                 thumb_dir: str = None,
                 hash_fn: Callable = None,
                 do_rot: bool = True,
                 old: bool = False,

                 log_level: int = logging.DEBUG,
                 timeout: int = 30):
        """
        Initialize the First Loop Worker

        :param identifier: The identifier of the worker
        :param log_level: The log level of the worker
        :param log_queue: The queue to log to
        :param cmd_queue: The command queue (arguments for the processing function)
        :param res_queue: The result queue (results of the processing function)
        :param timeout: The timeout for the worker

        :param compress: Whether to compress the images
        :param do_hash: Whether to hash the images
        :param target_size: The target size of the images
        :param shift_amount: The amount to shift the image before hashing
        :param thumb_dir: The directory to store the thumbnails
        :param hash_fn: The hash function to use
        :param do_rot: Whether to rotate the images before hashing
        :param old: Whether to use the old hashing method per default.

        Info about hash_fn:
        The hash function can be one of two types:
        - A function that takes a string and returns a string (old hashing method)
        - A function that takes a numpy array and returns a string (new hashing method)

        The old hashing method has been deprecated and is using the file system for hashing. It takes the path to the
        compressed image as an argument, computes the hash and returns it. The new hashing method takes a numpy array
        and computes the hash of that. The old method was slower and only used because I couldn't find a way to hash
        the numpy arrays consistently with rotation.
        """
        super().__init__(identifier=identifier,
                         log_queue=log_queue,
                         cmd_queue=cmd_queue,
                         res_queue=res_queue,
                         log_level=log_level,
                         timeout=timeout)

        if do_hash is False and compress is False:
            raise ValueError("At least one of do_hash or compress must be True")

        self.old = old
        self.do_hash = do_hash
        self.compress = compress
        self.shift_amount = shift_amount
        self.thumb_dir = thumb_dir
        self.target_size = target_size
        self.do_rot = do_rot

        if hash_fn is not None:
            self.hash_fn = hash_fn
        else:
            if self.old:
                self.hash_fn = util.hash_file
            else:
                self.hash_fn = util.hash_np

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value: bool):
        if value:
            self.logger.warning("Using old hashing method. "
                                "This method is deprecated and will be removed in the future.")

        self.__old = value


    def prep_logging(self, level: int = logging.DEBUG, q: mp.Queue = None):
        """
        Prepare the logging for the child process
        """
        self.logger = logging.getLogger(f"FirstLoopWorker_{self.identifier:03}")
        self.logger.setLevel(level)
        self.log_queue = q

        # Need to clear the handlers
        self.logger.handlers.clear()
        q_handler = QueueHandler(q)
        self.logger.addHandler(q_handler)

    def set_processing_function(self):
        """
        Set the first loop function to the correct function based on the configuration
        """
        if self.do_hash and self.compress:
            self.processing_fn = self.compress_and_hash
        elif self.do_hash:
            self.processing_fn = self.compute_hash
        elif self.compress:
            self.processing_fn = self.compress_only
        else:
            raise ValueError("At least one of do_hash or compress must be True")

    def compute_hash(self, arg: PreprocessArg) -> PreprocessResult:
        """
        Compute only the hash for a given image.

        :param arg: The PreprocessArg containing the file path
        """
        try:
            img, sz = imgp.load_std_image(img_path=arg.file_path, target_size=self.target_size, resize=True)
            if self.old:
                self.hash_fn: Callable[[str], str]
                h0, h90, h180, h270 = imgp.compute_img_hashes(image_mat=img,
                                                              temp_dir=self.thumb_dir,
                                                              temp_name=f"{self.identifier}_temp.png",
                                                              shift_amount=self.shift_amount,
                                                              hash_fn=self.hash_fn)
            else:
                self.hash_fn: Callable[[str], str]
                h0, h90, h180, h270 = imgp.hash_np_array(image_mat=img,
                                                         hash_fn=self.hash_fn,
                                                         shift_amount=self.shift_amount)

            return PreprocessResult(key=arg.key, hash_0=h0, hash_90=h90, hash_180=h180, hash_270=h270,
                                    org_x=sz[0], org_y=sz[1])
        except Exception as e:
            self.logger.error(f"Error in processing batch: {e}")
            tb = traceback.format_exc()
            return PreprocessResult(key=arg.key, error=tb)

    def compress_only(self, arg: PreprocessArg) -> PreprocessResult:
        """
        Compute the thumbnail for a given image.

        :param arg: The PreprocessArg containing the file path
        """
        try:
            img, sz = imgp.load_std_image(img_path=arg.file_path, target_size=self.target_size, resize=True)
            imgp.store_image(img, os.path.join(self.thumb_dir, f"{arg.key}.png"))
            return PreprocessResult(key=arg.key, org_x=sz[0], org_y=sz[1])
        except Exception as e:
            self.logger.error(f"Error in processing batch: {e}")
            tb = traceback.format_exc()
            return PreprocessResult(key=arg.key, error=tb)

    def compress_and_hash(self, arg: PreprocessArg):
        """
        Compute hash and store thumbnail.

        :param arg: The PreprocessArg containing the file path
        """
        try:
            img, sz = imgp.load_std_image(img_path=arg.file_path, target_size=self.target_size, resize=True)
            if self.old:
                h0, h90, h180, h270 = imgp.compute_img_hashes(image_mat=img,
                                                              temp_dir=self.thumb_dir,
                                                              temp_name=f"{self.identifier}_temp.png",
                                                              shift_amount=self.shift_amount,
                                                              hash_fn=self.hash_fn,
                                                              do_rot=self.do_rot)
            else:
                h0, h90, h180, h270 = imgp.hash_np_array(image_mat=img,
                                                         hash_fn=self.hash_fn,
                                                         shift_amount=self.shift_amount,
                                                         do_rot=self.do_rot)
            imgp.store_image(img, os.path.join(self.thumb_dir, f"{arg.key}.png"))

            return PreprocessResult(key=arg.key,
                                    org_x=sz[0], org_y=sz[1],
                                    hash_0=h0, hash_90=h90, hash_180=h180, hash_270=h270)
        except Exception as e:
            self.logger.error(f"Error in processing batch: {e}")
            tb = traceback.format_exc()
            return PreprocessResult(key=arg.key, error=tb)


class SecondLoopWorker(ChildProcess):
    has_dir_b: bool
    target_size: Optional[Tuple[int, int]] = None

    ram_cache: Dict[int, bytes]
    make_plots: bool = False
    plot_dir: Optional[str] = None
    plot_threshold: Optional[float] = None
    delta_fn: Callable[[np.ndarray[np.uint8], np.ndarray[np.uint8], bool], float]
    match_aspect_by: Optional[float] = None
    match_hash: bool = False
    do_rot: bool = True

    cache_key: Optional[int] = None
    cache: Optional[BatchCache] = None

    processing_fn: Callable[[SecondLoopArgs], SecondLoopResults] = None

    def __init__(self,
                 identifier: int,
                 cmd_queue: mp.Queue,
                 res_queue: mp.Queue,
                 log_queue: mp.Queue,

                 compare_fn: Callable[[np.ndarray[np.uint8], np.ndarray[np.uint8], bool], float],
                 target_size: Tuple[int, int],
                 has_dir_b: bool = False,
                 ram_cache: Dict[int, bytes] = None,
                 plot_dir: str = None,
                 plot_threshold: float = None,
                 hash_short_circuit: bool = False,
                 match_aspect_by: Optional[float] = None,
                 make_plots: bool = False,
                 do_rot: bool = True,

                 log_level: int = logging.DEBUG,
                 timeout: int = 30):
        """
        Initialize the Second Loop Worker

        :param identifier: The identifier of the worker
        :param log_level: The log level of the worker
        :param log_queue: The queue to log to
        :param cmd_queue: The command queue (arguments for the processing function)
        :param res_queue: The result queue (results of the processing function)
        :param timeout: The timeout for the worker

        :param compare_fn: Function that takes thw two images and a bool and computes a metric of difference
        :param target_size: The target size of the images
        :param has_dir_b: Whether we have a directory b
        :param ram_cache: The ram cache to use
        :param plot_dir: The directory to store the plots in
        :param plot_threshold: The threshold for the plot (can be different from the threshold for the comparison)
        :param hash_short_circuit: Whether to short circuit if the hashes match (hash matches -> no comparison)
        :param match_aspect_by: == 1, match the pixel in x and y, > 1, match the aspect ratio by a factor
        :param make_plots: Whether to make plots of the differences
        :param do_rot: Whether to rotate the images before comparing

        Info about match_aspect_by:
        If a value > 1.0 is chosen, the computation performed is the following:
        For image a and image b, the x / y ration is computed. The inverse is taken if the ratio is smaller than 1.
        Those normalized values are then compared as follows:
        a * factor >= b >= a / factor
        If b is not in the interval, the images are considered not-matching

        Info about compare_fn:
        The function should take three arguments:
        - The first image as a numpy nd.array
        - The second image as a numpy nd.array
        - A boolean whether to rotate the image before comparing
        Rotation is to be understood as rotating the image by 90 degrees three times and comparing the result.
        And taking the min in the default implementation. You can provide any function which takes these three
        arguments.
        """

        super().__init__(identifier=identifier,
                         log_queue=log_queue,
                         cmd_queue=cmd_queue,
                         res_queue=res_queue,
                         log_level=log_level,
                         timeout=timeout)

        # Flags
        self.has_dir_b = has_dir_b
        self.target_size = target_size
        self.ram_cache = ram_cache
        self.plot_dir = plot_dir
        self.plot_threshold = plot_threshold
        self.make_plots = make_plots

        self.delta_fn = compare_fn
        self.match_hash = hash_short_circuit
        self.match_aspect_by = match_aspect_by
        self.do_rot = do_rot

        if make_plots:
            if plot_threshold is None or plot_dir is None:
                raise ValueError("Plot Threshold and Plot dir needed for plotting.")

        self.fetch_x = 0
        self.fetch_y = 0

        self.set_processing_function()

    def prepare_cache(self, cache_key: Union[int, None]):
        """
        Update the Cache we have in the worker. If it's a new cache, we copy it for speed
        """
        if self.cache_key != cache_key and self.ram_cache is not None:
            self.cache_key = cache_key
            self.cache = pickle.loads(copy.deepcopy(self.ram_cache[self.cache_key]))

    def match_aspect_ratio_by(self, x: Tuple[int, int], y: Tuple[int, int]) -> bool:
        """
        Matches the aspect ratio within a certain interval
        """
        xa = x[0] / x[1] if x[0] > x[1] else x[1] / x[0]
        ya = y[0] / y[1] if y[0] > y[1] else y[1] / y[0]

        assert xa >= 1, "Aspect Ratio is less than 1"
        assert ya >= 1, "Aspect Ratio is less than 1"

        match = xa * self.match_aspect_by >= ya >= xa / self.match_aspect_by
        # return xa * self.match_aspect_by >= ya >= xa / self.match_aspect_by
        return match

    @staticmethod
    def match_px(x: Tuple[int, int], y: Tuple[int, int]) -> bool:
        """
        Matches the pixel size within a certain interval

        :returns True if the pixel size matches
        """
        a = x[0] == y[0] and x[1] == y[1]
        b = x[1] == y[0] and x[0] == y[1]
        r = a or b
        # return (x[0] == y[0] and x[1] == y[1]) or (x[1] == y[0] and x[0] == y[1])
        return r

    @staticmethod
    def determine_hash_match(x: Tuple[int, int, int, int], y: Tuple[int, int, int, int]) -> bool:
        """
        Short circuit if the hashes match
        """
        l = len(set(x) & set(y))
        # return len(set(x) & set(y)) > 0
        return l > 0

    def get_image_from_cache(self, key: int, is_x: bool = True) -> np.ndarray[np.uint8]:
        """
        Get an image from the cache

        :param key: The key of the image (so the key from the directory table)
        :param is_x: Whether we are looking for the x or y image (determines the cache we're going to use
        :kwargs: Additional arguments to match a call from the generic_fetch_image method

        :return: The image from the cache
        """
        if self.ram_cache is None:
            raise ValueError("Cache is not set")

        if is_x:
            return self.cache.x.get_image(key)
        else:
            return self.cache.y.get_image(key)

    def make_plot(self, diff: float, x_path: str, y_path: str, x: int, y: int):
        """
        Make a plot for a given set of images

        :param diff: The difference between the images
        :param x_path: The path to the first image
        :param y_path: The path to the second image
        :param x: key of x image
        :param y: key of y images

        :return: None
        """
        img_a_org = imgp.load_org_image(path=x_path)

        img_b_org = imgp.load_org_image(path=y_path)

        imgp.make_dif_plot(min_diff=diff,
                           img_a=os.path.basename(x_path),
                           img_b=os.path.basename(y_path),
                           mat_a=img_a_org,
                           mat_b=img_b_org,
                           store_path=os.path.join(self.plot_dir, f"{x}_{y}.png"))

    def process_batch_thumb(self, arg: SecondLoopArgs) -> SecondLoopResults:
        """
        Process a batch of images and return the results in the BatchCompareResult format
        Intended for cases when thumbnails exist or when we have a ram cache

        :param arg: The arguments for the batch
        :return: The results of the batch
        """
        self.prepare_cache(arg.cache_key)

        # Get the size we need to walk for the batch
        if self.has_dir_b:
            start = arg.y
        else:
            start = arg.x + 1 if arg.y <= arg.x else arg.y

        limit = arg.y + arg.y_batch

        # Prepare the diffs and errors
        diffs = []
        errors = []

        try:
            s = datetime.datetime.now(datetime.UTC)
            img_a = self.get_image_from_cache(key=arg.x, is_x=True)
            self.fetch_x += (datetime.datetime.now(datetime.UTC) - s).total_seconds()

            for i in range(start, limit):
                try:
                    s = datetime.datetime.now(datetime.UTC)
                    img_b = self.get_image_from_cache(key=i, is_x=False)
                    self.fetch_y += (datetime.datetime.now(datetime.UTC) - s).total_seconds()

                    # Using array equality to avoid expensive computation
                    if np.array_equal(img_a, img_b):
                        diffs.append((arg.x, i, 1, 0.0))

                    # Check hash
                    if self.match_hash:
                        if self.determine_hash_match(arg.x_hashes, arg.y_hashes[i - start]):
                            diffs.append((arg.x, i, 2, 0.0))

                            # Make a plot if necessary
                            if self.make_plots:
                                self.make_plot(diff=0,
                                               x_path=arg.x_path,
                                               y_path=arg.y_path[i - start],
                                               x=arg.x,
                                               y=i)

                            continue

                    # We have 0.0 -> means match the pixels
                    if self.match_aspect_by is not None and self.match_aspect_by == 0.0:
                        if not self.match_px(arg.x_size, arg.y_size[i - start]):
                            diffs.append((arg.x, i, 3, -1.0))
                            continue

                    # We have match-aspect of > 1.0 -> means match the aspect ratio
                    if self.match_aspect_by is not None and self.match_aspect_by >= 1.0:
                        if not self.match_aspect_ratio_by(arg.x_size, arg.y_size[i - start]):
                            diffs.append((arg.x, i, 3, -1.0))
                            continue

                    # Compute the diff and add it to the results
                    diff = self.delta_fn(img_a, img_b, self.do_rot)

                    # Make a plot if necessary
                    if self.make_plots and diff <= self.plot_threshold:
                        self.make_plot(diff=diff,
                                       x_path=arg.x_path,
                                       y_path=arg.y_path[i - start],
                                       x=arg.x,
                                       y=i)

                    diffs.append((arg.x, i, 1, diff))

                except Exception as e:
                    self.logger.exception(f"Error in processing Tuple: {arg.x}, {i}", exc_info=e)
                    tb = traceback.format_exc()
                    diffs.append(-1)
                    errors.append((arg.x, i, tb))

            return SecondLoopResults(x=arg.x,
                                     cache_key=arg.cache_key,
                                     success=diffs,
                                     errors=errors)

        except Exception as e:
            self.logger.error(f"Error with image x in batch {arg.x}: {arg.cache_key}", exc_info=e)
            tb = traceback.format_exc()
            # errors = [(arg.x, -1, tb)]
            errors = [(arg.x, i, tb) for i in range(start, limit)]
            return SecondLoopResults(x=arg.x,
                                     cache_key=arg.cache_key,
                                     success=[],
                                     errors=errors)

    def set_processing_function(self):
        """
        Set the processing function based on the configuration
        """
        self.processing_fn = self.process_batch_thumb

    def prep_logging(self, level: int = logging.DEBUG, q: mp.Queue = None):
        """
        Prepare the logging for the child process
        """
        self.logger = logging.getLogger(f"SecondLoopWorker_{self.identifier:03}")
        self.logger.setLevel(level)
        self.log_queue = q

        # Need to clear the handlers
        self.logger.handlers.clear()
        q_handler = QueueHandler(q)
        self.logger.addHandler(q_handler)

    def get_stats(self):
        """
        Print Timing Statistics for Debugging
        """
        b = super().get_stats()
        b += f"\nFetching X Took: {self.fetch_x}\nFetching Y Took: {self.fetch_y}"
        return b
