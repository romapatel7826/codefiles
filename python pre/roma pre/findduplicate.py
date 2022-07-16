
#using method

l = [10, 20, 30, 40, 50, 60, 70, 20, 30]
d = []

for ele in l:
    if l.count(ele)>1 and ele not in d:
        d.append(ele)
print(d)

# without using any method

l = [10, 20, 30, 40, 50, 60, 70, 20, 30]
d= []

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i]==l[j] and l[i] not in d:
           d.append(l[i])

print(d)


