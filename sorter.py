import args
import numpy as np


def mode_index():
    """Returns an index value based on user mode"""
    modes = {'H': 0, 'S': 1, 'V':2, 'R': 0, 'G': 1, 'B':2}

    return modes[args.mode.upper()]

def quicksort(partition_array, m):
    """Sorts partition using np.argsort"""
    sorted_partition = partition_array[partition_array[:,m].argsort()]
    if args.reverse:
        sorted_partition = sorted_partition[::-1]

    return sorted_partition


def partition(row, thresh_row):
    """Takes group of consecutive white pixels and sends them to quicksort."""
    m = mode_index()
    sorted_row = np.empty((0, 3), np.uint8)
    partition_array = np.empty((0, 3), np.uint8)


    for p, t in zip(row, thresh_row):
        if t[2] == 255:
            partition_array = np.append(partition_array, np.array([p]), axis=0)

        else:
            if len(partition_array) >= 1:
                sorted_partition = quicksort(partition_array, m)
                sorted_row = np.append(sorted_row, np.array(sorted_partition), axis=0)
                sorted_row = np.append(sorted_row, np.array([p]), axis=0)
            else:
                sorted_row = np.append(sorted_row, np.array([p]), axis=0)
            partition_array = np.empty((0, 3), int)

    if len(partition_array) >= 1:
        sorted_partition = quicksort(partition_array, m)
        sorted_row = np.append(sorted_row, np.array(sorted_partition), axis=0)

    return sorted_row

def sort_pixels(row, thresh_row):
    """Each row in image data is sorted and stacked back int one image."""
    sorted_pixels = np.empty((0,3), np.uint8)
    sorted_row = partition(row, thresh_row)
    sorted_pixels = np.vstack((sorted_pixels, sorted_row))

    return sorted_pixels
