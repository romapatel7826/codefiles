# n! = 1 X 2 X  3 x 4 .......n! 

from math import factorial


num = int(input("enter your number: "))

factorial = 1
for i in range(1, num+1):
    factorial = factorial * i

print(f"the factorial of {num} is {factorial}")