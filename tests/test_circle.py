def test_circle_positive(radius):
        r = Rectangle(radius, side_b)
        assert r.name == 'Rectangle'
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter

@pytest.mark.parametrize('radius,
                         [    -10,
                              10,
                              0,
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