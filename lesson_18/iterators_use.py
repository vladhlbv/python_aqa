from lesson_18.iterators import EvenIterator
from lesson_18.iterators import ReverseIterator


item_max: int = 12
print(f"Even generator for item up to {item_max}")
for item in EvenIterator(item_max):
    print(item)


data_list: list[int] = [0, 7, 15, 29, 35, 52, 55]
reverse_iter = ReverseIterator(data_list)
print(f"\nReverse generator for numbers of :{data_list}")

for item in reverse_iter:
    print(item)