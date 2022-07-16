# mylist = [80,10,20,30,100,40,50,60,70,90]
# mylist.sort()
# print(mylist)

# print("first largest number in the list",mylist[-1])
# print("second largest number in the list",mylist[-2])


#method 2
mylist = [80,10,20,30,100,40,50,60,70,90]

new_list =set (mylist)
print(new_list)

new_list.remove(max(new_list))
print(new_list)

print(max(new_list))