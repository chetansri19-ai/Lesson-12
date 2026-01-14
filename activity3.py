#Writing a program that takes an input(which has to be a minimum of 4 digits long) from the user and finds the middle number and then uses the number after the middle number and finds the product of the middle number and the number after it(using the multiplaction symbol and not addition).

num=int(input("Enter a number: "))
t=num
numLen=0

#iterate the loop
while t>0:
 numLen=numLen+1
 t=int(t/10)

 if numLen>=4:  #condition 1
  numLen=int(numLen/2)
  
  chk=0

  while num>0: #iterate loop
   rem=num%10
   if chk==numLen:
    midOne=rem
   elif chk==numLen-1:
    MidTwo=rem
   num=int(num/10)
   chk=chk+1
  prod= midOne*MidTwo
  print("The product of the middle number",midOne,"and the number after it",MidTwo,"is:",prod)
 else:
    print("Invalid Input.")