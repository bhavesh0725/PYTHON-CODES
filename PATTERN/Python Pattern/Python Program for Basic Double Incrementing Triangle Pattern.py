n=int(input("Enter no. of rows :"))
m=int(input("Enter no. to start off: "))
for i in range(n):
  for j in range(i+1):
    print(m,end=" ")
    m=m+1
  print()


# Enter no. of rows :4
# Enter no. to start off: 3
# 3 
# 4 5 
# 6 7 8 
# 9 10 11 12 