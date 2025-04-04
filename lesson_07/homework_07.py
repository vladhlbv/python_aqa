# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number + 2:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

# multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_func(numb_1, numb_2):
    rslt = numb_1 + numb_2
    print(str(numb_1) + "+" + str(numb_2) + "=" + str(rslt))

sum_func(int(input("Please input number 1:\n")), int(input("Please input number 2:\n")))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def avg_numb(numb_list):
    result = sum(numb_list) / len(numb_list)
    print("Average number of list " + str(numb_list) + " is " + str(result))

avg_numb([1,2,3,4,5])

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def str_reverse(new_str):
    string_rev: str = new_str[::-1]
    print("Reverse of the string " + str(new_str) + " is " + str(string_rev))

str_reverse(input("Please type your string:\n"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(new_words):
    lng_word = max(new_words, key=len)
    print("Longest word is:", lng_word)

longest_word(['Kateryna', 'Andrii', 'Mariya', 'Yevhen', 'Valentyn', 'Vlad'])

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    if str2 in str1:
        return str1.find(str2)
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7

def unique_ten_chars(new_string):
    new_string_set: set = set(new_string)
    if len(new_string_set) > 10:
        print("True")
    else:
        print("False")

unique_ten_chars(input("Please type something here:\n"))

# task 8

def even_sum(num_list):
    even_num_sum: int = sum(number for number in num_list if number % 2 == 0)
    print("Sum of even numbers in the list is:", even_num_sum)

even_sum([1, 10, 34, 81, 22, 5, 7, 24, 57, 2])

# task 9

def str_cont_h(user_inp):
    find_h: int = user_inp.find('h')
    while find_h == -1:
        user_inp: str = input("Input any word with letter H or h:\n").lower()
        find_h: int = user_inp.find('h')

str_cont_h(input("Input any word with letter H or h:\n").lower())

# task 10

def str_from_list(lst1):
        lst2: list = []
        for value in lst1:
            if type(value) == str:
                lst2.append(value)
        print(lst2)

str_from_list(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""