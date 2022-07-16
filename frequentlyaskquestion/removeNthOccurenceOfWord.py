from tkinter.font import ROMAN


mylist = ["roma","for", "roma", "roma","roma"]
word = "roma"
n=3
count=0
for i in range(0,len(mylist)-1):
    if(mylist[i]==word):
        count=count+1
    if(count==n):
        del mylist[i]
print("updated list",mylist)