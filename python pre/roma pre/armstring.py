from ast import Num


num = int(input("enter num "))
s = 0
temp = num

while temp > 0:
    c = temp % 10
    s += c**3
    temp //= 10

if num == s:
    print("armstrong num")
else:
    print(" not an armstrong")
