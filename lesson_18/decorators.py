# Декоратори:
from lesson_18.logger_setup import console_logger


# Напишіть декоратор, який логує аргументи та результати викликаної функції.
def logging_decorator (func):
    def wrapper(*args, **kwargs):
        console_logger.info(f"Function was called with arguments: {args}, or keyed arguments: {kwargs}")
        result = func(*args,**kwargs)
        console_logger.info(f"Function returned: {result}")
        return result
    return wrapper


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def exception_decorator (func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError as e:
            print(f"Division by zero is forbidden: {e}")
    return wrapper