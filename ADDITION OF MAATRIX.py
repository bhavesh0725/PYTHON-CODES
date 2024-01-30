a=[[1,2,3],
   [2,4,5],
   [1,0,5],
   [6,0,8]]

b= [[1,7,4],
   [7,3,9],
   [6,4,2],
   [2,5,7]]

result =[[0,0,0],
   [0,0,0],
   [0,0,0],
   [0,0,0]]


print(len(a))
print(len(a[0]))


for i in range(len(a)):
  for j in range(len(a[0])):
    result[i][j]= a[i][j]+b[i][j]

for r in result:
  print(r)
