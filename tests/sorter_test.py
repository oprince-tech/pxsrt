import numpy as np
import pytest

from pxsrt.sorter import mode_index
from pxsrt.sorter import partition
from pxsrt.sorter import quicksort
from pxsrt.sorter import sort_pixels
from pxsrt.sorter import sort_worthy


def test_sort_worthy():
    thresh_data = np.zeros((1, 5, 3))
    assert sort_worthy(thresh_data) is False


def test_sort_worthy_fail():
    thresh_data = np.full((1, 5, 3), 255)
    assert sort_worthy(thresh_data) is True


@pytest.mark.parametrize(
    ('input', 'expected'),
    (
        ('H', 0),
        ('S', 1),
        ('V', 2),
        ('R', 0),
        ('G', 1),
        ('B', 2),
    ),
)
def test_mode_index(input, expected):
    assert mode_index(input) == expected


@pytest.mark.parametrize(
    ('input', 'error_type'),
    (
        ('T', KeyError),
        ([], TypeError),
    ),
)
def test_mode_index_fail(input, error_type):
    with pytest.raises(error_type):
        mode_index(input)


@pytest.mark.parametrize(
    ('data', 'm', 'reverse'),
    (
        (
            np.array([[0, 50, 100], [25, 75, 125], [10, 20, 30]]),
            2,
            False,
        ),
    ),
)
def test_quicksort_type_integrity(data, m, reverse):
    assert type(quicksort(data, m, reverse)) == np.ndarray


@pytest.mark.parametrize(
    ('data', 'm', 'reverse', 'expected'),
    (
        (
            np.array([[0, 50, 100], [25, 75, 125], [10, 20, 30]]),
            2,
            False,
            np.array([[10, 20, 30], [0, 50, 100], [25, 75, 125]]),
        ),
        (
            np.array([[0, 50, 100], [25, 75, 125], [10, 20, 30]]),
            2,
            True,
            np.array([[25, 75, 125], [0, 50, 100], [10, 20, 30]]),
        ),
        (
            np.array([[0, 50, 100], [25, 75, 125], [10, 20, 30]]),
            0,
            False,
            np.array([[0, 50, 100], [10, 20, 30], [25, 75, 125]]),
        ),
    ),
)
def test_quicksort(data, m, reverse, expected):
    assert np.testing.assert_array_equal(
        quicksort(data, m, reverse),
        expected,
    ) is None


@pytest.mark.parametrize(
    ('row', 'thresh_row', 'mode', 'reverse', 'full_sort', 'expected'),
    (
        (
            np.array([[0, 50, 100], [25, 75, 125], [10, 20, 30]]),
            np.array([[0, 0, 255], [0, 0, 255], [0, 0, 255]]),
            'V',
            False,
            True,
            np.array([[10, 20, 30], [0, 50, 100], [25, 75, 125]]),
        ),
        (
            np.array([[0, 50, 100], [25, 75, 125], [10, 20, 30]]),
            np.array([[0, 0, 255], [0, 0, 255], [0, 0, 255]]),
            'H',
            False,
            True,
            np.array([[0, 50, 100], [10, 20, 30], [25, 75, 125]]),
        ),
    ),
)
def test_partition_full(row, thresh_row, mode, reverse, full_sort, expected):
    assert np.testing.assert_array_equal(
        partition(
            row,
            thresh_row,
            mode,
            reverse,
            full_sort,
        ),
        expected,
    ) is None


sort_halves = pytest.mark.parametrize(
    ('row', 'thresh_row', 'mode', 'reverse', 'full_sort', 'expected'),
    (
        (
            np.array(
                [[0, 0, 5], [0, 0, 1], [0, 0, 4], [0, 0, 3], [0, 0, 2]],
            ),
            np.array(
                [[0, 0, 255], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 255]],
            ),
            'V',
            False,
            False,
            np.array(
                [[0, 0, 1], [0, 0, 5], [0, 0, 4], [0, 0, 3], [0, 0, 2]],
            ),
        ),
    ),
)

not_sort_worthy = pytest.mark.parametrize(
    ('row', 'thresh_row', 'mode', 'reverse', 'full_sort', 'expected'),
    (
        (
            np.array(
                [[0, 0, 5], [0, 0, 1], [0, 0, 4], [0, 0, 3], [0, 0, 2]],
            ),
            np.array(
                [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
            ),
            'V',
            False,
            False,
            np.array(
                [[0, 0, 5], [0, 0, 1], [0, 0, 4], [0, 0, 3], [0, 0, 2]],
            ),
        ),
    ),
)


@sort_halves
def test_partition_nonfull(
    row, thresh_row, mode,
    reverse, full_sort, expected,
):
    assert np.testing.assert_array_equal(
        partition(row, thresh_row, mode, reverse, full_sort),
        expected,
    ) is None


@sort_halves
def test_sort_pixels_worth(
    row, thresh_row, mode,
    reverse, full_sort, expected,
):
    assert np.testing.assert_array_equal(
        sort_pixels(row, thresh_row, mode, reverse, full_sort),
        expected,
    ) is None


@not_sort_worthy
def test_sort_pixels_nworth(
    row, thresh_row, mode,
    reverse, full_sort, expected,
):
    assert np.testing.assert_array_equal(
        sort_pixels(row, thresh_row, mode, reverse, full_sort),
        expected,
    ) is None
