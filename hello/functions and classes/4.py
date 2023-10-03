# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# result = list(filter(None,list1))
# print(result)

list1 = ["Mike","","Emma","Kelly","","Brad"]
result =[ i for i in list1 if i !=  ""]
print(result)
