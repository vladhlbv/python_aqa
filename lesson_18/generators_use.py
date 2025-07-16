from lesson_18.generators import even_generator
from lesson_18.generators import fibonacci_generator

for item in even_generator(14):
    print(item)

for number in fibonacci_generator(50):
    print(number)