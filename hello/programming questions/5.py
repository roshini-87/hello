def count(str):
    char = {}
    for i in str:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1
    for char, count in char.items():
        print(f"'{char}': {count}")

str = input("Enter a string: ")

count(str)
