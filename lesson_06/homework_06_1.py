new_string: str = input("Please type something here:")

unique_symbols: set = set()

for value in new_string:
    unique_symbols.add(value)

while len(unique_symbols) > 10:
    print("True")
    break
else:
    print("False")