class Student:
    def __init__(self, first_name: str, last_name: str, age: int, avg_mark: float = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.__avg_mark = avg_mark

    def get_info(self):
        return f"Student First Name: {self.first_name}, Last Name: {self.last_name}, Age: {self.age}"

    def return_avg_mark(self):
        return self.__avg_mark

    def set_avg_mark(self, amount:float):
        self.__avg_mark = amount

    def increase_avg_mark(self, amount:float):
        self.__avg_mark += amount

    def decrease_avg_mark(self, amount: float):
        self.__avg_mark -= amount