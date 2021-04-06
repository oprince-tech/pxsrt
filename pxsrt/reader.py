import numpy as np


def read_thresh(
    data: np.ndarray,
    L: int,
    U: int,
    outer: bool,
    mode: str,
) -> np.ndarray:
    """
    Creates a threshold map from image data and desire threshold range (0-255).
    """

    thresh_data = np.copy(data)

    if outer:
        thresh_data[thresh_data < L] = 255
        thresh_data[thresh_data >= U] = 255
        thresh_data[thresh_data != 255] = 0

    else:
        thresh_data[thresh_data <= L] = 0
        thresh_data[thresh_data > U] = 0
        thresh_data[thresh_data != 0] = 255

    if mode == 'H' or mode == 'R':
        thresh_data = np.flip(thresh_data, axis=2)
        thresh_data[:, :, :2] = 0
    elif mode == 'S' or mode == 'G':
        thresh_data = np.roll(thresh_data, 1, axis=2)
        thresh_data[:, :, :2] = 0
    else:
        thresh_data[:, :, :2] = 0

    return thresh_data
