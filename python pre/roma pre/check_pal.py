def pal(num):
    x1 = num[::-1]

    if num == x1:
        print("pali")
    else:
        print("no")

print(pal('121'))