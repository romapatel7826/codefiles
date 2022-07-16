#using for loop(done by me)


mylist = [1,2,3,4,5]
total=1

for i in range(0,len(mylist)):
    total = total * mylist[i]
print("multiplication of all element", total)

#using for loop
mylist = [1,2,3,4,5]
result=1
for x in mylist:
    result = result*x
print("multiplication of all element", result)

#using numpy
import numpy
mylist = [1,2,3,4,5]
result=numpy.prod(mylist)
print(result)