from lesson_18.decorators import logging_decorator
from lesson_18.decorators import exception_decorator


@logging_decorator
def multiply(a: int | float, b: int | float) -> int | float:
    return a * b

@exception_decorator
def divide(a: int | float, b: int | float) -> int | float:
    return a / b


if __name__ == '__main__':
    multiply(a = 5, b = 15)

    divide(a = 5, b = 0)