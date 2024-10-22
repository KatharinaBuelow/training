import pytest
from .. import add_one, add_two


@pytest.mark.parametrize("x, y", [(1, 2), (2, 3), (3, 4)])
def test_add_one(x, y):
    assert y == add_one(x)

@pytest.mark.parametrize("x, y", [(1, 3), (2, 4), (3, 5)])
def test_add_two(x, y):
    assert y == add_two(x)
   
