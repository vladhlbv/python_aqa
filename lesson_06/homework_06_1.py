new_string: str = input("Please type something here:")

new_string_set: set = set(new_string)

if len(new_string_set) > 10:
    print("True")
else:
    print("False")