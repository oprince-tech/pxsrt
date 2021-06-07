import sys

import pytest

from pxsrt.args import parse_args


def test_no_arg_Image_failure():
    sys.argv = ['pxsrt']
    with pytest.raises(SystemExit):
        args = parse_args()  # noqa: F841


def test_args_is_dict():
    sys.argv = ['pxsrt', 'test.jpg']
    args = parse_args()
    assert isinstance(args, dict)


def test_args_defaults():
    sys.argv = ['pxsrt', 'test.jpg']
    args = parse_args()
    expected = {
        'input_image': 'test.jpg',
        'mode': 'V',
        'direction': 'h',
        'L_threshold': 0,
        'U_threshold': 255,
        'outer': False,
        'reverse': False,
        'preview': False,
        'save': False,
    }
    assert args == expected


@pytest.mark.parametrize(
    'input',
    (
        pytest.param(['pxsrt', 'test.jpg', '-m', 'F'], id='Invalid_mode (F)'),
        pytest.param(['pxsrt', 'test.jpg', '-m', '0'], id='Invalid_mode (0)'),
        pytest.param(
            ['pxsrt', 'test.jpg', '-d', 'G'],
            id='Invalid_direction (G)',
        ),
        pytest.param(['pxsrt', 'test.jpg', 'T', 'A'], id='Invalid_extra_args'),
        pytest.param(['pxsrt', 'test.jpg', '-g'], id='Invalid_flag'),
    ),
)
def test_invalid_args(input):
    sys.argv = input
    with pytest.raises(SystemExit):
        args = parse_args()  # noqa: F841
