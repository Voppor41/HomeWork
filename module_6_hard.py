import math

class Figure:

    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.__sides = sides
        self.filled = False

    def get_color(self):
        return print(self.__color)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)\

    def get_sides(self):
        return self.__sides[0]

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)
        self.__radius = radius

    def get_squre(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], int) and new_sides[0] > 0:
            self._sides = new_sides[0]
            self.__radius = new_sides[0] / (2 * math.pi)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)

    def get_squre(self):
        a, b, c = self._sides
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides_lenght):
        super().__init__(color, sides_lenght)
        self.set_sides(sides_lenght)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], int) and new_sides[0] > 0:
            self._sides = [new_sides[0] * self.sides_count]

    def get_volume(self):
        return self._sides[0]**3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

