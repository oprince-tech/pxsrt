from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from pxsrt import args
from pxsrt import utils
from pxsrt.utils import check_dir_integrity
from pxsrt.utils import create_save_filename
from pxsrt.utils import generate_preview
from pxsrt.utils import save_sort


class MyMock:
    def mock_args():
        return {
            'input_image': 'test.jpg',
            'mode': 'V',
            'direction': 'h',
            'L_threshold': 0,
            'U_threshold': 255,
            'outer': False,
            'reverse': False,
            'preview': True,
            'save': False,
        }

    def save_filename(**args):
        return 'test.jpg'


@pytest.fixture
def mock_continue_original_args(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    monkeypatch.setattr(args, 'parse_args', MyMock.mock_args)


@pytest.fixture
def mock_input_new_args(monkeypatch):
    inputs = iter(['n', 10, 20, 'n', 'V', 'y'])
    monkeypatch.setattr(args, 'parse_args', MyMock.mock_args)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))


@pytest.fixture
def mock_invalid_L_threshold(monkeypatch):
    inputs = iter(['n', 'A', 'n', 10, 20, 'n', 'V', 'y'])
    monkeypatch.setattr(args, 'parse_args', MyMock.mock_args)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))


@pytest.fixture
def mock_invalid_mode(monkeypatch):
    inputs = iter(['n', 10, 20, 'n', 't'])
    monkeypatch.setattr(args, 'parse_args', MyMock.mock_args)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))


@pytest.fixture
def mock_save_y_autoname(monkeypatch):
    inputs = iter(['y', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))


@pytest.fixture
def mock_save_y_custom(monkeypatch):
    inputs = iter(['y', 'MyCustomName.jpg'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))


@pytest.fixture
def mock_save_n(monkeypatch):
    inputs = iter(['n'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))


@pytest.fixture
def mock_save_filename(monkeypatch):
    inputs = iter(['y', ''])
    monkeypatch.setattr(utils, 'create_save_filename', MyMock.save_filename)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))


def test_input_continue_thresh_data(mock_continue_original_args):
    data = np.asarray(
        [[[0, 50, 100], [25, 75, 125], [10, 20, 30]]], dtype=np.uint8,
    )
    thresh_data = np.asarray(
        [[[0, 0, 255], [0, 0, 255], [0, 0, 255]]], dtype=np.uint8,
    )
    returned_thresh_data, final_args = generate_preview(data, thresh_data)
    assert np.testing.assert_array_equal(
        returned_thresh_data, thresh_data,
    ) is None


def test_input_continue_final_args(mock_continue_original_args):
    data = np.asarray(
        [[[0, 50, 100], [25, 75, 125], [10, 20, 30]]], dtype=np.uint8,
    )
    thresh_data = np.asarray(
        [[[0, 0, 255], [0, 0, 255], [0, 0, 255]]], dtype=np.uint8,
    )
    returned_thresh_data, final_args = generate_preview(data, thresh_data)
    assert final_args == {
        'threshold': [0, 255],
        'outer': False,
        'mode': 'V',
    }


def test_new_thresh_data(mock_input_new_args):
    data = np.asarray(
        [[[0, 50, 100], [25, 75, 125], [10, 20, 30]]], dtype=np.uint8,
    )
    thresh_data = np.asarray(
        [[[0, 0, 255], [0, 0, 255], [0, 0, 255]]],  dtype=np.uint8,
    )
    expected = np.asarray([[[0, 0, 0], [0, 0, 0], [0, 0, 0]]],  dtype=np.uint8)
    returned_thresh_data, final_args = generate_preview(data, thresh_data)
    assert np.testing.assert_array_equal(
        returned_thresh_data, expected,
    ) is None


def test_input_new_args(mock_input_new_args):
    data = np.asarray(
        [[[0, 50, 100], [25, 75, 125], [10, 20, 30]]], dtype=np.uint8,
    )
    thresh_data = np.asarray(
        [[[0, 0, 255], [0, 0, 255], [0, 0, 255]]], dtype=np.uint8,
    )
    returned_thresh_data, final_args = generate_preview(data, thresh_data)
    assert final_args == {
        'threshold': [10, 20],
        'outer': False,
        'mode': 'V',
    }


def test_input_L_threshold_error(mock_invalid_L_threshold, capfd):
    data = np.asarray(
        [[[0, 50, 100], [25, 75, 125], [10, 20, 30]]], dtype=np.uint8,
    )
    thresh_data = np.asarray(
        [[[0, 0, 255], [0, 0, 255], [0, 0, 255]]], dtype=np.uint8,
    )
    generate_preview(data, thresh_data)
    out, err = capfd.readouterr()
    assert out == "ValueError: invalid literal for int() with base 10: 'A'\n"


def test_input_mode_error(mock_invalid_mode, capfd):
    data = np.asarray(
        [[[0, 50, 100], [25, 75, 125], [10, 20, 30]]], dtype=np.uint8,
    )
    thresh_data = np.asarray(
        [[[0, 0, 255], [0, 0, 255], [0, 0, 255]]], dtype=np.uint8,
    )
    try:
        generate_preview(data, thresh_data)
    except Exception:
        out, err = capfd.readouterr()
        assert out == (
            'ValueError: Mode not accepted. '
            'Please choose from (H, S, V, R, G, B).\n'
        )


@pytest.mark.parametrize(
    'arg, expected', [
        (
            {
                'input_image': 'test.jpg',
                'mode': 'V',
                'direction': 'h',
                'L_threshold': 0,
                'U_threshold': 255,
                'outer': False,
                'reverse': False,
            }, 'test_Vh(0-255)FalseFalse.jpg',
        ),
        (
            {
                'input_image': 'test.png',
                'mode': 'R',
                'direction': 'v',
                'L_threshold': 100,
                'U_threshold': 200,
                'outer': True,
                'reverse': True,
            }, 'test_Rv(100-200)TrueTrue.png',
        ),
    ],
)
def test_create_save_filename_autoname(arg, expected, mock_save_y_autoname):
    save_filename = create_save_filename(**arg)
    assert save_filename == expected


@pytest.mark.parametrize(
    'arg, expected', [
        (
            {
                'input_image': 'test.jpg',
                'mode': 'V',
                'direction': 'h',
                'L_threshold': 0,
                'U_threshold': 255,
                'outer': False,
                'reverse': False,
            }, 'MyCustomName.jpg',
        ),
    ],
)
def test_create_save_filename_custom(arg, expected, mock_save_y_custom):
    save_filename = create_save_filename(**arg)
    assert save_filename == expected


@pytest.mark.parametrize(
    'arg, expected', [
        (
            {
                'input_image': 'test.jpg',
                'mode': 'V',
                'direction': 'h',
                'L_threshold': 0,
                'U_threshold': 255,
                'outer': False,
                'reverse': False,
            }, None,
        ),
    ],
)
def test_create_save_filename_abort(arg, expected, mock_save_n):
    save_filename = create_save_filename(**arg)
    assert save_filename is None


@pytest.fixture(scope='session')
def mock_image_file(tmpdir_factory, **args):
    img = Image.open('/home/oli/projects/pxsrt/images/tokyo.jpg')
    fn = tmpdir_factory.mktemp('data').join('test.jpg')
    img.save(str(fn))
    return fn


@pytest.mark.parametrize(
    'arg, expected', [
        (
            {
                'input_image': 'test.jpg',
                'mode': 'V',
                'direction': 'h',
                'L_threshold': 0,
                'U_threshold': 255,
                'outer': False,
                'reverse': False,
            }, None,
        ),
    ],
)
def test_save_sort(arg, expected, mock_image_file, mock_save_filename):
    output_image = Image.open(Path(mock_image_file))
    save_sort(output_image, **arg)
    assert Path('/home/oli/projects/pxsrt/pxsrt_exports/test.jpg').is_file()


def test_check_dir_integrity():
    t = Path('./test_temp_directory/')
    check_dir_integrity(t)
    t.rmdir()
