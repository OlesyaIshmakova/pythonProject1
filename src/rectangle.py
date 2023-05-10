from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        if side_a <= 0 or side_b <= 0:
            raise ValueError(f'Expected side_a and side_b > 0, got {side_a}, {side_b}')
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'Rectangle'

    #
    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
