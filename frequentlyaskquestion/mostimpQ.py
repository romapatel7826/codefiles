mylist = "aaaabbbccc"

new_list = mylist.split(',')
# print(new_list)
visited = []
final_list = []
for ch in mylist:
    if ch not in visited:
        final_list.append(f"{ch}:{mylist.count(ch)}")
        visited.append(ch)
print(final_list)

print(",".join(final_list))




# Python program to print  
# ASCII Value of Character 
  
# In c we can assign different 
# characters of which we want ASCII value  
  

a = "roma"
print(type("a").__name__)


str = "roma"
print(str +' patel')