adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawyer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawyer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

print("Basic text:\n", adventures_of_tom_sawyer)

adventures_of_tom_sawyer: str = adventures_of_tom_sawyer.replace("\n", " ")
print("Task 1:",adventures_of_tom_sawyer)

# task 02 ==
""" Замініть .... на пробіл
"""

adventures_of_tom_sawyer: str = adventures_of_tom_sawyer.replace("....", " ")
print("Task 2:",adventures_of_tom_sawyer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

splitted: list = adventures_of_tom_sawyer.split()
# print("Splitted:", splitted)
adventures_of_tom_sawyer: str = ' '.join(splitted)
print("Task 3:",adventures_of_tom_sawyer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
value_to_find: str = "h"
counter: int = 0

for value in adventures_of_tom_sawyer:
    if value == value_to_find:
        counter += 1

print(f"Літера {value_to_find} зустрічається в тексті", counter,"разів.")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
splitted: list = adventures_of_tom_sawyer.split()
counter: int = 0

for value in splitted:
    if value.istitle():
        counter += 1

print(counter,"слів у тексті починається з великої літери.")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
value_to_find: str = "Tom"

first_index: int = adventures_of_tom_sawyer.find(value_to_find)
second_index: int = adventures_of_tom_sawyer.find(value_to_find, first_index + 1)

print("Tom зустрічається вдруге на позиції:",second_index)

# task 07
""" Розділіть змінну adventures_of_tom_sawyer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawyer_sentences
"""
adventures_of_tom_sawyer_sentences = None

adventures_of_tom_sawyer_sentences: list = adventures_of_tom_sawyer.split(". ")
print(adventures_of_tom_sawyer_sentences)

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawyer_sentences.
Перетворіть рядок у нижній регістр.
"""
index_sent: int = 3
sent_by_index: str = adventures_of_tom_sawyer_sentences[index_sent]
print(sent_by_index)

sent_by_index_lower: str = sent_by_index.lower()
print(sent_by_index_lower)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
value_to_find: str = "By the time"

for sentence in adventures_of_tom_sawyer_sentences:
    if sentence.startswith(value_to_find):
        print(f"Речення :{sentence} починається з фрази :{value_to_find}")

# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawyer_sentences.
"""
index_sent: int = -1
sent_by_index: str = adventures_of_tom_sawyer_sentences[index_sent]

sent_splitted: list = sent_by_index.split()

counter: int = 0

for word in sent_splitted:
    counter += 1

print(f"Останнє речення складається з {counter} слів.")