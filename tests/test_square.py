import pytest
from src.square import Square

@pytest.mark.parametrize('side_a, area, perimeter',
                         [
                             (16, 100, 40),
                             (2, 4, 8),
                        ])
def test_square_positive(side_a, area, perimeter):
    r = Square(side_a)
    assert r.name == 'Square'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

@pytest.mark.parametrize('side_a', [-18, 0])
def test_rectangle_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)