# using for loop

mylist = [4,6,7,8,8]
total=0

for i in range(0,len(mylist)):
    total = total + mylist[i]
print("sum of all element", total)

#using sum() method:

mylist = [4,6,7,8,8]
total=0

total=sum(mylist)
print("sum of all element", total)