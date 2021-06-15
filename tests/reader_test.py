import numpy as np
import pytest

from pxsrt.reader import read_thresh


def test_array_shape_integrity():
    data = np.ndarray(shape=(10, 10, 3))
    assert read_thresh(
        data=data,
        L=0,
        U=255,
        outer=False,
        mode='V',
    ).shape == data.shape


def test_array_shape_failure():
    data = np.ndarray(shape=(100, 100))
    with pytest.raises(IndexError):
        read_thresh(
            data=data,
            L=0,
            U=255,
            outer=False,
            mode='V',
        )


def test_return_array_type():
    data = [[[0, 0, 0], [0, 0, 0]]]
    assert type(
        read_thresh(
            data=data,
            L=0,
            U=255,
            outer=False,
            mode='V',
        ),
    ) == np.ndarray


def test_outer_bounds():
    data = np.zeros(shape=(1, 1, 3))
    thresh_data = read_thresh(
        data=data,
        L=100,
        U=255,
        outer=True,
        mode='V',
    )
    expected = np.asarray([[[0, 0, 255]]], dtype=np.uint8)
    assert np.testing.assert_array_equal(thresh_data, expected) is None


@pytest.mark.parametrize(
    ('data', 'L', 'U', 'outer', 'mode', 'expected'),
    (
        (
            np.full((1, 1, 3), 100),
            0,
            255,
            False,
            'V',
            np.asarray([[[0, 0, 255]]]),
        ),
        (
            np.full((1, 1, 3), 100),
            101,
            255,
            False,
            'R',
            np.asarray([[[0, 0, 0]]]),
        ),
        (
            np.full((1, 1, 3), 255),
            0,
            255,
            False,
            'S',
            np.asarray([[[0, 0, 255]]]),
        ),
        (
            np.full((1, 1, 3), 255),
            0,
            100,
            False,
            'V',
            np.asarray([[[0, 0, 0]]]),
        ),
    ),
)
def test_inner_bounds(data, L, U, outer, mode, expected):
    assert np.testing.assert_array_equal(
        read_thresh(data, L, U, outer, mode),
        expected,
    ) is None


@pytest.mark.parametrize(
    ('data', 'L', 'U', 'outer', 'mode', 'expected'),
    (
        (
            np.full((1, 1, 3), 50),
            100,
            200,
            True,
            'V',
            np.asarray([[[0, 0, 255]]]),
        ),
        (
            np.full((1, 1, 3), 100),
            0,
            255,
            True,
            'R',
            np.asarray([[[0, 0, 0]]]),
        ),
    ),
)
def test_outer_bound(data, L, U, outer, mode, expected):
    assert np.testing.assert_array_equal(
        read_thresh(data, L, U, outer, mode),
        expected,
    ) is None
