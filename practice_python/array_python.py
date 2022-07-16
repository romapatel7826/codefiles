from array import *
stu_roll = array('i', [11, 12, 13, 14, 15, 16, 17])
print("print original array")
n = len(stu_roll)
for i in range(n):
    print(i, "=", stu_roll[i])

print("********************")
a = stu_roll[1:6]
for i in a:
    print(i)