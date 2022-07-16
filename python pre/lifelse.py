
# if-elif-else ladder
# a = 30
# if(a>3):
#         print(" the value is greater than 3")
# elif(a>9):
#         print("the value is greater than 9")
# elif(a<20):
#         print("the value is less than 20")
# else:
#     print("value is not grester than 3 or 9")
# print("done")
# multiple if-else statement


# a = 30
# if(a>3):
#         print(" the value is greater than 3")
# if(a>9):
#         print("the value is greater than 9")
# if(a<20):
#         print("the value is less than 20")
# else:
#     print("value is not grester than 3 or 9")
# print("done")


# ifelse quize


# age = int(input("enter your age "))

# if (age > 18):
#     print("yes")
# else:
#     print("no")

# boolean operators

# age = int(input("enter your age "))
# if(age>24 and age<56):
#     print("you can work with us")

# is_in in python

from mailbox import NotEmptyError
from tkinter.messagebox import YES


# a = None
# if(a is None):
#     print("yes")

# s = [2, 45, 67, 8,]
# if(457 in s):
#     print("true")
# else:
#     print("false")

# else is optional
# a = 200
# if(a<100):
#     print("true")
# elif(a<101):
#     print("yes or no")
# else:
#     print("else is optional")

num1 = int(input("enter number 1"))
num2 = int(input("enter number 2"))
num3 = int(input("enter number 3"))
num4 = int(input("enter number 4"))

if(num1>num4):
    f1 = num1

else: 
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3

if(f1>f2):
    print(str(f1) + "  is gratest")
else:
    print(str(f2) + "  is greatest")