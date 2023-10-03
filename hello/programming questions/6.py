def function():
    for i in range(n):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        height = float(input("Enter score : "))
        d.append((name, age, height))

n = int(input("Enter the number of tuples: "))
d = []
function()
sorted_data = sorted(d, key=lambda x: (x[0], x[1], x[2]))
print("\nSorted Tuples:")
for i in sorted_data:
    print([(f" ({i[0]}), ({i[1]}), ({i[2]})")])
