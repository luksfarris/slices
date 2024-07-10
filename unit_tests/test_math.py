import pytest

from slices.sample_math import sample_sum


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (2, 3, 5),
        (3, 4, 7),
        (4, 5, 9),
        (5, 6, 11),
    ],
)
def test_sample_sum(a: int, b: int, expected: int) -> None:
    assert sample_sum(a, b) == expected
