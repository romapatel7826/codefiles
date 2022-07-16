
# using temp variable swap

mylist = [23,45,67,78,89]
size=len(mylist)

temp = mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp

print("value after swap", mylist)

#without using temp bariable swap

mylist[0], mylist[-1]=mylist[-1],mylist[0]

print("after swap value is ", mylist)

#using tuple to swap two num

get=(mylist[-1],mylist[0])
mylist[0],mylist[-1]=get

print("value after swapping ", mylist)



