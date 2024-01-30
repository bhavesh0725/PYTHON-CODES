def armstrongNo(lower,upper):
  for i in range(lower, upper):
    temp=i
    sum=0
    order= len(str(i))
    while temp >0:
      digit = temp %10
      sum += (digit ** order)
      temp = temp//10
    if sum == i :
      print(i) 
      

   
    
      


def main():
 
  lower= int(input("Enter the lower limit: "))
  upper= int(input("Enter the upper limit: "))
  armstrongNo(lower,upper)

if __name__ == "__main__":
  main()
