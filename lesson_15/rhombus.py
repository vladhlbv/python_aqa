class Rhombus:
    def __init__(self, side_a: int, angle_a: int = 1):
        self.__side_a = side_a
        self.__angle_a = angle_a
        self.__angle_b = 180 - angle_a
        self.__angle_c = self.__angle_a
        self.__angle_d = self.__angle_b

    def __setattr__(self, key, value):
        if (key == "angle_a" or key == "angle_b" or key == "angle_c" or key == "angle_d") and value <= 0:
            raise ValueError(f"{key} value should be greater than 0 degrees")
        print(f"Setting attribute {key} to value {value}")
        super().__setattr__(key, value)

    def __str__(self):
        return f"Rhombus Side A: {self.__side_a},Rhombus Angle A: {self.__angle_a}, Angle B: {self.__angle_b}, Angle C: {self.__angle_c}, Angle D: {self.__angle_d}"