
n= int (input("Enter the value of n: "))
m = int(input("ente the value of m: "))

for i in range(n):

  for j in range(i+1): # this for loop for printing the spaces 
    print(" ",end=" ")


  for j in range(0,m): ### this for loop for printing the star 
    print("*",end=" ")

  print()
