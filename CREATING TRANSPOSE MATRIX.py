def transposeMatrix(TM):
  for i in range(rows):
    for j in range(cols):
      TM[j][i] = M1[i][j]
  return TM

      
def createMatrix(N,M): 
  mainList=[]
  for i in range(N):
    subList=[]
    for j in range(M):
      element = int(input(f"Enter the element at [{i+1}] th row and [{j+1}] th column"))
      subList.append(element)
    mainList.append(subList)
  return mainList




if __name__ == "__main__":
  rows=int(input("Enter the no. of rows: "))
  cols= int(input("Enter the no. of cols: "))


  M1= createMatrix(rows, cols)
  print("before transpose")
  for i in M1:
    print(i)
  print("*********************")

  print("Creating zero matrix: ")
  TM= createMatrix(cols, rows)


  print(" After Transposing of matrix: ")
  TM=transposeMatrix(TM)

  for i in TM:
    print(i)
  

  


 



 

