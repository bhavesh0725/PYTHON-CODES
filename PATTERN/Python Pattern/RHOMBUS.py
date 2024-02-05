
n=int(input("Enter the value of n "))
for i in range(n):
  

  for j in range(i+1): # this for loop for printing the spaces 
    print(" ",end=" ")


  for j in range(0,n): ### this for loop for printing the star 
    print("*",end=" ")

  print()


  #   output:
  #   Enter the value of n: 4
  #     * * * * 
  #       * * * * 
  #         * * * * 
  #           * * * * 
