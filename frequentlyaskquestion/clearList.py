
#using clear()

# mylist = [2,4,5,6,8,7,9,5]
# print("list before clear",mylist)
# mylist.clear()
# print("list after clear",mylist)

# using mylist=[](initialize list with no value)
# mylist = [2,4,5,6,8,7,9,5]
# print("list before clear",mylist)
# mylist=[]
# print("list after clear",mylist)

#using '*=0' this method remove all the element from the list
  
# mylist = [2,4,5,6,8,7,9,5]
# print("list before clear",mylist)
# mylist *=0
# print("list after clear",mylist)

#using del method

mylist = [2,4,5,6,8,7,9,5]
# print("list before clear",mylist)
# del mylist[:]
# print("list after clear",mylist)

#practice
del mylist[:]

print(mylist)
