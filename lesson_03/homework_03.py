alice_in_wonderland: str = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area: int = 436402
azov_sea_area: int = 37800

total_area: int = black_sea_area + azov_sea_area

print("Total area of Black and Azov seas:",total_area,"sq km.")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
items_total: int = 375291
wh1_wh2_items_total: int = 250449
wh2_wh3_items_total: int = 222950

wh1_items_total: int = items_total - wh2_wh3_items_total
wh3_items_total: int = items_total - wh1_wh2_items_total
wh2_items_total: int = items_total - wh1_items_total - wh3_items_total

print("First warehouse stores:",wh1_items_total,"items.")
print("Second warehouse stores:",wh2_items_total,"items.")
print("Third warehouse stores:",wh3_items_total,"items.")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
payment_per_month: int = 1179
payment_duration_months: int = 18

total_payment: int = payment_per_month * payment_duration_months

print("Total PC cost is:", total_payment,"UAH.")

# task 07
"""
Знайди остачу від ділення чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a: int = 8019 % 8
b: int = 9907 % 9
c: int = 2789 % 5
d: int = 7248 % 6
e: int = 7128 % 5
f: int = 19224 % 9

print("Modulus division a:",a)
print("Modulus division b:",b)
print("Modulus division c:",c)
print("Modulus division d:",d)
print("Modulus division e:",e)
print("Modulus division f:",f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

large_pizza: int = 274
mid_pizza: int = 218
juice: int = 35
cake: int = 350
water: int = 21

food_total: int = (large_pizza * 4) + (mid_pizza * 2) + (juice * 4) + cake + (water * 3)

print("Total food order:",food_total,"UAH.")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photo_total: int = 232
photo_per_page: int = 8

pages_used: int = photo_total // photo_per_page

print("Ihor should use:",pages_used,"pages.")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

trip_length: int = 1600
fuel_consumption: int = 9
fuel_tank_vol: int = 48

trip_fuel_used: float = trip_length * fuel_consumption / 100
trip_stops_count: int = int(trip_fuel_used // fuel_tank_vol)

print("Total fuel consumption per trip:",trip_fuel_used,"liters.")
print("Total fuel refill stops per trip:",trip_stops_count,"times.")