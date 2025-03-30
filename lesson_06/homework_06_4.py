# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

num_list: list = [1, 10, 34, 81, 22, 5, 7, 24, 57, 2]

even_num_sum: int = sum(number for number in num_list if number % 2 == 0)

print("Sum of even numbers in the list is:", even_num_sum)