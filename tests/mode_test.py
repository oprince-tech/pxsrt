from typing import Any

import pytest

from pxsrt.mode import target_mode


@pytest.mark.parametrize(
    ('input', 'expected'),
    (
        ('H', 'HSV'),
        ('S', 'HSV'),
        ('V', 'HSV'),
        ('R', 'RGB'),
        ('G', 'RGB'),
        ('B', 'RGB'),
    ),
)
def test_target_mode(input, expected):
    assert target_mode(input) == expected


@pytest.mark.parametrize(
    ('input', 'error_type'),
    (
        (1, KeyError),
        ('ABC', KeyError),
        ([], TypeError),
        ((), KeyError),
    ),
)
def test_target_mode_exceptions(input: Any, error_type) -> None:
    with pytest.raises(error_type):
        target_mode(input)
