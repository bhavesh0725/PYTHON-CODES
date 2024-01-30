def factorial(N):
  if N<0:
    return "Not defined"
  elif N<2:
    return 1
  else:
    return N*factorial(N-1)

def main():

  n= int(input("Enter the no : "))
  
  print(factorial(n))

if __name__ == "__main__":
  main()
