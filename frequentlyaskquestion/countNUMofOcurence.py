list = [11,34,5,6,77,56,4,3,3,77,34,5,11]

new_list  = []

for num in list:
    if list.count(num)==1:
        new_list.append(num)
print(new_list)