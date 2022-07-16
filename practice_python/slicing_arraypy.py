# from array import *
# roll = array('i', [1, 3, 5,  7, 5, 7, 8, 9,])
# print("original_data")
# n = len(roll)
# for i in range(n):
#     print(i, "=", roll[i] )

# print("*********")
# a = roll[-4:-8]
# for i in a:
#     print(i)

from array import *
roll = array('i', [1, 3, 5,  7, 5, 7, 8, 9,])
for i in roll[0:8:2]:
    print(i)