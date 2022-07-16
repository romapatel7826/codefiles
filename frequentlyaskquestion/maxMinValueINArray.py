arr = [10,40,29,50,35,53]
#for finding max element in array
max = arr[0] 
n=len(arr)
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)


# for finding min value in array
arr = [10,40,29,50,35,53]
min=arr[0]

for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print(min)


