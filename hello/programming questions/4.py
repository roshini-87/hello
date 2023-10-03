# matrix addition
# a=[[1,2],
#    [5,7]]
# b=[[9,8],
#    [4,6]]
# result=[[0,0],
#         [0,0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         result[i][j]=a[i][j]+b[i][j]

# for r in result:
#     print(r)


# matrix transpose

# c=[[1,5],
# [3,7]]
# result = [[0,0],
# [0,0]]
# for i in range(len(c)):
#     for j in range(len(c[0])):
#         result[j][i]=c[i][j]

# for r in result:
#     print(r)

# matrix multiplication

a=[[1,2],
   [5,7]]
b=[[9,8],
   [4,6]]
res=[[0,0],
     [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            res[i][j]+= a[i][k]*b[k][j]

for r in res:
    print(r)