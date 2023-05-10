import pytest
from src.circle import Circle
def test_rectangle_positive(side_a, side_b, area, perimeter):
        r = Rectangle(side_a, side_b)
        assert r.name == 'Circle'
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter

@pytest.mark.parametrize('side_a, side_b',
                         [    (-10, 20),
                              (1, -2),
                              (0, -2),
                              (0, 0),
                         ])
def test_rectangle_negative(side_a, side_b):
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b)

def test_rectangle_positive_2():
        r = Rectangle(10, 20)
        assert r.name == 'Rectangle'
        assert r.get_area() == 200
        r.side_a = 20
        assert r.get_area() == 400