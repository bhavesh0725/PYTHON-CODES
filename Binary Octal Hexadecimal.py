def numbersystem(decimal):
  binary = bin(decimal)
  octal = oct(decimal)
  hexadecimal = hex(decimal)
  
  return binary, octal, hexadecimal
  

def main():

  n= int(input("Enter the decimal no. : "))
  
  
  binary, octal , hexadecial = numbersystem(n)
  print("Binary: ",binary) #prefix : 0b
  print("Octal: ",octal) # prefix : 0o
  print("hexadecimal: ", hexadecial)  #prefix : 0x

if __name__ == "__main__":
  main()
