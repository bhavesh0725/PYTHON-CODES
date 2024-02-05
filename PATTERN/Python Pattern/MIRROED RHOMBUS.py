
n= int (input("Enter the value of n: "))

for i in range(n):
  for j in range(i,n-1):
    print(" ",end=" ")

  for j in range(n):
    print("*",end=" ")

  print()


# Enter the value of n: 4
#       * * * * 
#     * * * * 
#   * * * * 
# * * * * 
