# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_generator(max_number: int):
    for i in range(0, max_number + 1, 2):
        yield i



# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci_generator(max_num: int):
    a = 0
    b = 1
    while a <= max_num:
        yield a
        a, b = b, a + b


# if __name__ == '__main__':