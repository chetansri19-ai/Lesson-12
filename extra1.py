#Writing a program to display the sum of odd numbers and even numbers that fall between 12 and 37 using nested loops.
sum_odd = 0
sum_even = 0
for num in range(12, 38):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Sum of even numbers between 12 and 37 is:", sum_even)
print("Sum of odd numbers between 12 and 37 is:", sum_odd)
