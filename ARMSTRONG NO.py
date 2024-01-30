def armstrongNo(n):
  sum=0
  temp=n
  order = len(str(n))

  while temp>0:
    digit= temp %10
    cube= digit ** order
    sum +=cube
    temp = temp// 10

  if sum == n:
    return (f"The no. {n} is armstrong no.")
  else:
    return (f"The no. {n} is not armstrong no.")


def  main():
  n= int(input("Enter the no:"))
  print(armstrongNo(n))

if __name__ == "__main__":
  main()
