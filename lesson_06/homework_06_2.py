# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

user_inp: str = str(input("Input any word with letter H or h:\n")).lower()
user_inp_low: str = user_inp.lower()
find_h: int = user_inp.find('h')

while find_h == -1:
    user_inp: str = str(input("Input any word with letter H or h:\n")).lower()
    find_h: int = user_inp.find('h')