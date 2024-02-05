
n= int (input("Enter the value of n: "))

for i in range(n):

  for j in range(i):
    print(" ",end=" ")
    
  for j in range((2*i),(2*n)-1):  # 0 ---> 7, (0,7)
                                    #1---->5   (2,7)
    print("*",end=" ")              #2---->3    (4,7)
                                    #3---->1   (6,7)
  print()
    
    
  # Enter the value of n: 9
  # * * * * * * * * * * * * * * * * * 
  #   * * * * * * * * * * * * * * * 
  #     * * * * * * * * * * * * * 
  #       * * * * * * * * * * * 
  #         * * * * * * * * * 
  #           * * * * * * * 
  #             * * * * * 
  #               * * * 
  #                 * 
