def product(a):
    a.sort()

    p1 = a[-1] * a[-2] * a[-3]  
    # p2 = a[0] * a[1] * a[-1]
    # return max(p1,p2)   
    return p1

data = []
n = int(input('Enter how many elements you want: '))
for i in range(0, n):
    x = int(input('Enter the numbers into the array: '))
    data.append(x)
print(data)


result = product(data)
print(result)
