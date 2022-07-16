# set is collection of non repeatative items
# we can not add list in set
# tuple we can add in set
# we can not add dictionary in set
# we can add unic value in set
a = { 1,  3, 5, 7, 8}
print(a)
print(type(a))

a = {} # it will create empty distionary not empty set

b = set()  #method to create empty set
b.add(2)
print(b)
b.add((2, 5, 6, 7))

print(len(b))
b.remove(2) # remove
b.remove(12) # throws error
