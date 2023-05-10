import abc
import math


class Figure(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def area(self):
        pass

    # Периметр — длина контура замкнутой плоской фигуры, длина границы (Википедия)
    # Периметр, оказывается, общее понятие и для прямолинейных и криволинейных фигур
    # В том числе периметр - это длина окружности (синоним "периметр окружности")
    # поэтому метод perimeter() переосмыслен - он будет возвращать кортеж (название контура, значение)
    # если периметр как обобщающее понятие для длины контура (границы) фигуры категорически не подходит,
    # можно переименовать этот метод, например, в "contour_length()"
    @abc.abstractmethod
    def perimeter(self):
        pass

    # метод calculator() - общий для всех с идентичной реализацией
    def calculator(self):
        print(f"______{self.__class__.__name__}______")
        result = self.perimeter() # получаем кортеж с названием контура и значением
        return f"{result[0]} is: {round(result[1], 3)}\nArea is: {round(self.area(), 3)}"

    def check_args(self, *args):  # универсальный метод для проверки параметров (не дублировать в наследниках)
    # сюда же можно добавить проверку аргументов на неотрицательность (опция)
        for v in args:
            if type(v) not in (int, float):
                raise ValueError(f"Wrong data type for {self.__class__.__name__}!")


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.sides = (side_a, side_b, side_c)  # сделал покомпактнее хранение параметров фигур
        self.check_args(*self.sides)

    def area(self):
        p = sum(self.sides) / 2
        return math.prod([p] + [p - s for s in self.sides])  # тоже покороче - произведение элементов списка

    def perimeter(self):
        return "Perimeter", sum(self.sides)  # возвращает кортеж с названием контура и значением


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.sides = (side_a, side_b)
        self.check_args(*self.sides)

    def area(self):
        return math.prod(self.sides)

    def perimeter(self):
        return "Perimeter", 2 * sum(self.sides)


class Square(Rectangle):  # В математике квадрат - это прямоугольник (наследуем квадрат от прямоугольника)
    def __init__(self, side_a, side_b=None):
        if side_b is None:
            side_b = side_a
        self.check_args(side_a, side_b)  # проверяем типы перед нахождением минимума, чтобы не возникла ошибка сравнения
        side = min(side_a, side_b)
        super().__init__(side, side)


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        self.check_args(self.radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return "Circumference", 2 * math.pi * self.radius  # Круг имеет не периметер, а длину окружности


if __name__ == '__main__':

    figures = [Circle(1.5), Square(10), Triangle(2, 2, 3), Triangle(1, 2, 3)]

    for i in figures:
        print(i.calculator())