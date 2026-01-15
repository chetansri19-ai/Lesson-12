#Write a program to accept numbers and check whether it is a perfect number or not.(Perfect number is positive integer which is equal to the sum of its divisors like divisors of 6 are 1,2,3 and the sum of them is 6)
num=int(input("Enter a positive integer: "))
sum_divisors=0
for i in range(1, num):
    if num % i == 0:
        sum_divisors += i
if sum_divisors == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")