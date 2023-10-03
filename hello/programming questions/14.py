a = [1, 2, 3, 4, 5]
result = 1
for i in a:
    result *= i

b = [result // i for i in a]
print(b)
