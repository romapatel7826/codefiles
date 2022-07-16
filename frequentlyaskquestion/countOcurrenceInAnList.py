
#using loop method



mylist = [2,5,6,7,8,9,5,6,5,5]
x=5
count=0
for ele in mylist:
    if(ele==x):
        count=count+1
print("{} has occurd {} times".format(x,count))

#uing count() method

mylist = [2,5,6,7,8,9,5,6,5,5]
x=5
print("{} has occurd {} times".format(x,mylist.count(x))) 

# using counter()

from collections import Counter
mylist = [2,5,6,7,8,9,5,6,5,5]
x=6

dic=Counter(mylist)
print("{} has occurd {} times".format(x,dic[x]))

