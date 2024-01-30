def matrix(rows, cols):
  mainList=[]
  for i in range(rows):
    subList=[]
    for j in range(cols):
      element = int(input(f"Enter the element at [{i+1}] th row and [{j+1}] th column"))
      subList.append(element)
    mainList.append(subList)
  return mainList

if __name__ == "__main__":
  rows=int(input("Enter the no. of rows: "))
  cols= int(input("Enter the no. of cols: "))
  
  
  result= matrix(rows, cols)
  for i in result:
    print(i)
    
    
