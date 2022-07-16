
# simple swap value

mylist = [34,6,78,45,67,89,12,23]
#print(mylist)

pos1, pos2 = 2,5

mylist[pos1], mylist[pos2] = mylist[pos2], mylist[pos1]

print("swap list is ", mylist)

# swap values using pop()

first_ele = mylist.pop(pos1)
sec_ele = mylist.pop(pos2-1)

mylist.insert(pos1,sec_ele)
mylist.insert(pos2,first_ele)

print(mylist)


# swap values using tuple

get=(mylist[pos1], mylist[pos2])
mylist[pos2],mylist[pos1]=get

print(mylist)
