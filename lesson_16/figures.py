import math
from lesson_16.figures_base import Figure


class Triangle(Figure):

    def __init__(self, side_length_1: int | float, side_length_2: int | float, side_length_3: int | float, angle_1: int | float):
        self.__side_length_1 = side_length_1
        self.__side_length_2 = side_length_2
        self.__side_length_3 = side_length_3
        self.__angle_1 = angle_1

    def return_side_length_1(self) -> int | float:
        return self.__side_length_1

    def return_side_length_2(self) -> int | float:
        return self.__side_length_2

    def return_side_length_3(self) -> int | float:
        return self.__side_length_3

    def return_angle_1(self) -> int | float:
        return self.__angle_1

    def calculate_area_of_figure(self) -> int | float:
        angle_rad = math.radians(self.return_angle_1())  # convert degrees to radians
        return (self.return_side_length_1() * self.return_side_length_2()) / 2 * math.sin(angle_rad)

    def calculate_perimeter_of_figure(self) -> int | float:
        return self.return_side_length_1() + self.return_side_length_2() + self.return_side_length_3()

    def __str__(self):
        return f"Triangle side 1 length: {self.return_side_length_1()}, side 2 length: {self.return_side_length_2()}, side 3 length: {self.return_side_length_3()}, angle 1 degrees: {self.return_angle_1()}"


class Circle(Figure):

    def __init__(self, circle_radius: int | float):
        self.__circle_radius = circle_radius

    def return_circle_radius(self) -> int | float:
        return self.__circle_radius

    def calculate_area_of_figure(self) -> int | float:
        return pow(math.pi * self.return_circle_radius(), 2)

    def calculate_perimeter_of_figure(self) -> int | float:
        return 2 * math.pi * self.return_circle_radius()

    def __str__(self):
        return f"Circle radius: {self.return_circle_radius()}"


class Diamond(Figure):

    def __init__(self, diamond_side_length: int | float, diamond_angle: int | float):
        self.__diamond_side_length = diamond_side_length
        self.__diamond_angle = diamond_angle

    def return_diamond_side_length(self) -> int | float:
        return self.__diamond_side_length

    def return_diamond_angle(self) -> int | float:
        return self.__diamond_angle

    def calculate_area_of_figure(self) -> int | float:
        diamond_angle_rad = math.radians(self.return_diamond_angle())  # convert degrees to radians
        return pow(self.return_diamond_side_length(), 2) * math.sin(diamond_angle_rad)

    def calculate_perimeter_of_figure(self) -> int | float:
        return 4 * self.return_diamond_side_length()

    def __str__(self):
        return f"Diamond side length: {self.return_diamond_side_length()}, diamond angle: {self.return_diamond_angle()}"