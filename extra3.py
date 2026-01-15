#Writing a program to print numbers from 1 to 20 except multiple of 2 and 3.
for num in range(1, 21):
    if num % 2 != 0 and num % 3 != 0:
        print(num)
        