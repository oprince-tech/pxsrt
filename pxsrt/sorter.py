import numpy as np


def mode_index(mode: str) -> int:
    """Returns an index value based on user mode"""
    modes = {'H': 0, 'S': 1, 'V': 2, 'R': 0, 'G': 1, 'B': 2}
    return modes[mode]


def quicksort(partition_array: np.ndarray,
              m: int,
              reverse: bool) -> np.ndarray:
    """Sorts partition using np.argsort"""
    sorted_partition = partition_array[partition_array[:, m].argsort()]
    if reverse:
        sorted_partition = sorted_partition[::-1]

    return sorted_partition


def partition(row: np.ndarray,
              thresh_row: np.ndarray,
              mode: str,
              reverse: bool) -> np.ndarray:
    """Takes group of consecutive white pixels and sends them to quicksort."""
    m = mode_index(mode)
    sorted_row = np.empty((0, 3), np.uint8)
    partition_array = np.empty((0, 3), np.uint8)

    for p, t in zip(row, thresh_row):
        if t[2] == 255:
            partition_array = np.append(partition_array,
                                        np.array([p]),
                                        axis=0)

        else:
            if len(partition_array) >= 1:
                sorted_partition = quicksort(partition_array, m, reverse)
                sorted_row = np.append(sorted_row,
                                       np.array(sorted_partition),
                                       axis=0)
                sorted_row = np.append(sorted_row,
                                       np.array([p]),
                                       axis=0)
            else:
                sorted_row = np.append(sorted_row,
                                       np.array([p]),
                                       axis=0)
            partition_array = np.empty((0, 3), int)

    if len(partition_array) >= 1:
        sorted_partition = quicksort(partition_array, m, reverse)
        sorted_row = np.append(sorted_row,
                               np.array(sorted_partition),
                               axis=0)

    return sorted_row


def sort_pixels(row: np.ndarray,
                thresh_row: np.ndarray,
                mode: str,
                reverse: bool) -> np.ndarray:
    """Each row in image data is sorted and stacked back int one image."""
    sorted_ndarray = np.empty((0, 3), np.uint8)
    sorted_row = partition(row, thresh_row, mode, reverse)
    sorted_ndarray = np.vstack((sorted_ndarray, sorted_row))

    return sorted_ndarray
