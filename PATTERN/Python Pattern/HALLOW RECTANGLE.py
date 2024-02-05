
n= int (input("Enter the value of n: "))
m = int(input("ente the value of m: "))

for i in range(n):
  for j in range(m):
    if i==0 or i==n-1 or j==0 or j==m-1:
      print("*",end=" ")

    else:
      print(" ",end=" ")

  print()
  # Enter the value of n: 4
  # ente the value of m:5
  # * * * * * 
  # *       * 
  # *       * 
  # * * * * * 

