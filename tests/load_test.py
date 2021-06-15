import numpy
import pytest

from pxsrt.load import load_image


def test_load_non_image():
    with pytest.raises(SystemExit):
        load_image(
            image='test.txt',
            target='HSV',
            mode='HSV',
            direction='h',
        )


def test_load_invalid_target():
    with pytest.raises(SystemExit):
        load_image(
            image='./images/tokyo.jpg',
            target='H',
            mode='HSV',
            direction='h',
        )


def test_data_ndarray():
    data = load_image(
        image='./images/tokyo.jpg',
        target='HSV',
        mode='HSV',
        direction='h',
    )
    assert type(data) == numpy.ndarray


def test_data_shape():
    data = load_image(
        image='./images/tokyo.jpg',
        target='HSV',
        mode='HSV',
        direction='h',
    )
    assert data.shape == (500, 750, 3)


def test_data_shape_rotated():
    data = load_image(
        image='./images/tokyo.jpg',
        target='HSV',
        mode='HSV',
        direction='v',
    )
    assert data.shape == (750, 500, 3)
