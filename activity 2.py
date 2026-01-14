#Writing a program to find out all the prime numbers(not divisible by any number but 1) in a given range by the input of user using nested loop.

range1=int(input("Enter the first number of the range:"))
range2=int(input("Enter the last number of the range:"))

print("The prime numbers between",range1,"and",range2,"are:")

for num in range(range1,range2+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
                print(num)
                break