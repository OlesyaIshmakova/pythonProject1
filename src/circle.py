from src.figure import Figure

class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f'Expected radius circle > 0, got {radius}')
        self.radius = radius
        self.name = 'Circle'
        self.area = 2 * 3.14 * radius * radius

    @staticmethod
    def check_if_can_create_circle(radius: int):
            if not (radius >= 0):
                raise ValueError(f'Radius must be greater than 0. got: {radius}')