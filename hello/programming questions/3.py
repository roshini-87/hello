def integers(a):
   value = str(a) + str(a+a) + str(a+a+a)
   return int(value)
num1 = int(input())
res = integers(num1)
print(res)