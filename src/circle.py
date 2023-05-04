class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError(f'Expected radius circle > 0, got {radius}')
        self.radius = radius
        self.name  = 'Circle'
        # self.area = side_a * side_b
        # self.perimeter = 2 * (side_a + side_b)
#