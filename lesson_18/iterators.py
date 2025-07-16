# Ітератор для зворотного виведення елементів списку.

class ReverseIterator:
    def __init__(self, iter_data: list):
        self.iter_data = iter_data
        self.index = len(iter_data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index -= 1
        return self.iter_data[self.index]


# Ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class EvenIterator:
    def __init__(self, max_num: int):
        self.max_num = max_num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current > self.max_num:
            raise StopIteration

        result = self.current
        self.current += 2
        return result