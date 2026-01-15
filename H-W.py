#Writing a program that converts a decimal number into a binary number.
num=float(input("Enter a decimal number: "))
binary=""
if num>=0:
 while num>0:
  rem=num%2
  binary=str(rem)+binary
  num=int(num/2)
 print("The binary equivalent is:",binary)
else:
    print("Invalid Input.")