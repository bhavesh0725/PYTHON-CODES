
n= int (input("Enter the value of n: "))

for i in range(n):
  for j in range(i+1):
    print("*",end=" ")

  print()
  
for i in range(n-1): 
  for j in range(i,n-1):
    print("*",end=" ")
  print()
  

# Enter the value of n: 4
# * 
# * * 
# * * * 
# * * * * 
# * * * 
# * * 
# * 
