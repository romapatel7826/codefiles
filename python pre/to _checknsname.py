from tkinter.font import names


names = ["roma", "seema", "rupesh", "ashish", "samaksh", "dhanvi"]
name = input("enter your name \n")

if name in names:
    print("your name is present in the list ")
else:
    print("your name is not present in the list")