# list1=[1,32,3,1,4,2,4,5,67]
# res = set(list1)
# print(list(set(res)))

def duplicates(remove):
    unique=[]
    for i in remove:
        if i not in unique:
            unique.append(i)
    return unique

list1=[1,12,1,3,2,3,2,54,8]
result= duplicates(list1)
print(result)