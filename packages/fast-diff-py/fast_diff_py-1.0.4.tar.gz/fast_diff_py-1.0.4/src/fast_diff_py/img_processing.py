import cv2
import numpy as np
import skimage
from typing import Tuple, Callable
import os


def load_org_image(path: str) -> np.ndarray[np.uint8]:
    """
    Get an original image from a path, do not resize

    :param path: Path to the image

    :return: The image as a numpy array
    """
    # Load the image
    img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)

    # Check the image is not grayscale
    if len(img.shape) == 2:
        img = skimage.color.gray2rgb(img)

    return img


def load_std_image(img_path: str, target_size: Tuple[int, int], resize: bool = True) -> (
        Tuple)[np.ndarray[np.uint8], Tuple[int, int]]:
    """
    Load an image from a path and return it as a numpy array

    Info: The image is not containing the alpha channel

    :param img_path: The path to the image to load
    :param target_size: The target size to resize the image to
    :param resize: Whether to resize the image to the target size

    :raises ValueError: If the image is not the correct size and resize is False
    """

    img = load_org_image(img_path)
    aspect = (img.shape[0], img.shape[1])

    if img.shape[0] != target_size[0] or img.shape[1] != target_size[1]:
        if resize:
            img = cv2.resize(img, dsize=target_size, interpolation=cv2.INTER_CUBIC)
        else:
            raise ValueError(f"Image {img_path} is not the correct size")
    return img, aspect


def hash_np_array(image_mat: np.ndarray,
                  hash_fn: Callable[[np.ndarray[np.uint8]], str],
                  shift_amount: int = 0,
                  do_rot: bool = True) -> Tuple[str, str, str, str]:
    """
    Compute a hash of an image matrix

    :param image_mat: The image matrix to compute the hash for
    :param hash_fn: The hash function to use
    :param shift_amount: The amount to shift the image before computing the hash (default 0)
    :param do_rot: Whether to rotate the image before computing the hash (default True)

    :return: The hash of the image matrix
    """
    assert 8 > shift_amount > -8, "amount exceeding range"

    # shift only if the amount is non-zero
    if shift_amount > 0:
        image_mat = np.right_shift(image_mat, shift_amount)
    elif shift_amount < 0:
        image_mat = np.left_shift(image_mat, abs(shift_amount))

    hash_0 = hash_fn(image_mat)

    hash_90 = hash_180 = hash_270 = None

    if do_rot:
        # Rot 90
        image_mat = np.rot90(image_mat, k=1, axes=(0, 1))
        hash_90 = hash_fn(image_mat)

        # Rot 180
        image_mat = np.rot90(image_mat, k=1, axes=(0, 1))
        hash_180 = hash_fn(image_mat)

        # Rot 270
        image_mat = np.rot90(image_mat, k=1, axes=(0, 1))
        hash_270 = hash_fn(image_mat)

    return hash_0, hash_90, hash_180, hash_270


def compute_img_hashes(image_mat: np.ndarray,
                       temp_dir: str,
                       temp_name: str,
                       shift_amount: int = 0,
                       hash_fn: Callable[[str], str] = None,
                       do_rot: bool = True) \
        -> Tuple[str, str, str, str]:
    """
    Compute hash_prefix for duplicate detection.

    Info:
        The hash_fn should take in a string as an argument which is the path to the file to hash.
        The hash should be returned as a string.

    :param image_mat: The image matrix to compute the hash_prefix for
    :param temp_dir: The directory to store the temporary files
    :param temp_name: The name prefix of the temporary files
    :param shift_amount: The amount to shift the image before computing the hash_prefix (default 0)
    :param hash_fn: The hash function to use (default sha1), can be altered.
    :param do_rot: Whether to rotate the image before computing the hash_prefix (default True)

    :return: Tuple of Hashes (0, 90, 180, 270)
    """
    # should be sanitized by the main process.
    assert 8 > shift_amount > -8, "amount exceeding range"

    # compute_new_paths
    path_hash_0 = os.path.join(temp_dir, f"{temp_name}_0.png")
    path_hash_90 = os.path.join(temp_dir, f"{temp_name}_90.png")
    path_hash_180 = os.path.join(temp_dir, f"{temp_name}_180.png")
    path_hash_270 = os.path.join(temp_dir, f"{temp_name}_270.png")

    # shift only if the amount is non-zero
    if shift_amount > 0:
        image_mat = np.right_shift(image_mat, shift_amount)
    elif shift_amount < 0:
        image_mat = np.left_shift(image_mat, abs(shift_amount))

    # store rot0 with shift
    cv2.imwrite(path_hash_0, image_mat)

    hash_90 = hash_180 = hash_270 = None

    if do_rot:
        # rot 90
        image_mat = np.rot90(image_mat, k=1, axes=(0, 1))
        cv2.imwrite(path_hash_90, image_mat)

        # rot 180
        image_mat = np.rot90(image_mat, k=1, axes=(0, 1))
        cv2.imwrite(path_hash_180, image_mat)

        # rot 270
        image_mat = np.rot90(image_mat, k=1, axes=(0, 1))
        cv2.imwrite(path_hash_270, image_mat)

        # need to compute file hash since writing the
        hash_90 = hash_fn(path_hash_90)
        hash_180 = hash_fn(path_hash_180)
        hash_270 = hash_fn(path_hash_270)

        # shouldn't be allowed to fail
        os.remove(path_hash_90)
        os.remove(path_hash_180)
        os.remove(path_hash_270)

    hash_0 = hash_fn(path_hash_0)

    # shouldn't be allowed to fail
    os.remove(path_hash_0)

    return hash_0, hash_90, hash_180, hash_270


def compute_image_diff(image_a: np.ndarray, image_b: np.ndarray, use_gpu: bool = False,
                       do_rot: bool = True) -> float:
    """
    Compute the mean squared error between two images. This is the standard implementation of this process

    :param image_a: The first image to compare
    :param image_b: The second image to compare
    :param use_gpu: Whether to use the GPU for the computation
    :param do_rot: Whether to rotate the image before computing the hash_prefix (default True)

    :return: The mean squared error between the two images
    """
    if use_gpu:
        import fast_diff_py.img_processing_gpu as gpu
        delta = gpu.mse_gpu(image_a, image_b)

        if do_rot:
            # Rotate image three times to find the best match
            for i in range(3):
                image_a = np.rot90(image_a, k=1, axes=(0, 1))
                delta = min(gpu.mse_gpu(image_a, image_b), delta)

    else:
        delta = mse(image_a, image_b)

        if do_rot:
            # Rotate image three times to find the best match
            for i in range(3):
                image_a = np.rot90(image_a, k=1, axes=(0, 1))
                delta = min(mse(image_a, image_b), delta)

    return delta


def mse(image_a: np.ndarray, image_b: np.ndarray) -> float:
    """
    The mean squared error, which is the base for the other metrics.

    :param image_a: The first image to compare
    :param image_b: The second image to compare

    :return: The mean squared error between the two images
    """
    assert image_a.shape == image_b.shape, "Images must be the same size"

    difference = image_a.astype("float") - image_b.astype("float")
    sq_diff = np.square(difference)
    sum_diff = np.sum(sq_diff)
    px_count = image_a.shape[0] * image_a.shape[1]
    return sum_diff / px_count


def make_dif_plot(min_diff: float,
                  img_a: str, img_b: str,
                  mat_a: np.ndarray, mat_b: np.ndarray,
                  store_path: str):
    """
    Create a Plot in case we have a difference high enough
    """
    import matplotlib.pyplot as plt
    fig = plt.figure()
    plt.suptitle(f"MSE: {min_diff:.2f}")

    # plot first image
    ax = fig.add_subplot(1, 2, 1)
    ax.title.set_text(img_a)
    plt.imshow(mat_a, cmap=plt.cm.gray)
    plt.axis("off")

    # plot second image
    ax = fig.add_subplot(1, 2, 2)
    ax.title.set_text(img_b)
    plt.imshow(mat_b, cmap=plt.cm.gray)
    plt.axis("off")

    # Don't show plot, clears the figure and an empty plot is aved.
    # plt.show(block=False)
    # show the images
    plt.savefig(store_path)
    plt.close()


def store_image(image: np.ndarray, path: str):
    """
    Store an image to a path
    """
    cv2.imwrite(path, image)
