class Figure:
    # def __init__(self):
    #     self.name =  'Figure'
    def get_area(self):
        pass

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return round(self.get_area() + figure.get_area(), 2)
            # return self.get_area() + figure.get_area()
        raise ValueError(f'Object {figure} is not subclass of Figure class')
