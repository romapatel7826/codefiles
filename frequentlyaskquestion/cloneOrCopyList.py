#using slicing
mylist = [4,6,7,8,4,7,5]
print(mylist)
mylist_copy=mylist[:]
print(mylist_copy)

# using extend( method)

mylist = [4,6,7,8,4,7,5]
print(mylist)
mylist_copy=[]
mylist_copy.extend(mylist)
print(mylist_copy)

#using list( method)
mylist = [4,6,7,8,4,7,5]
print(mylist)
mylist_copy=[]
mylist_copy=list(mylist)
print(mylist_copy)

#using copy()

mylist = [4,6,7,8,4,7,5]
print(mylist)
mylist_copy=mylist.copy()
print(mylist_copy)

# using list comprehensive

mylist = [4,6,7,8,4,7,5]
print(mylist)
mylist_copy=[i for i in mylist]
print(mylist)