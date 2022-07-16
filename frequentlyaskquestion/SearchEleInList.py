
list = [2,4,6,7,89,2,4,]

ele = 4
flag=0
for i in list:
    if(i==ele):
        print("element found")
        flag=1
        break
if(flag==0):
    print("element not found")

# using in operator

list = [2,4,6,7,89,2,4,]

ele = 2

if(ele in list):
    print("element found")
else:
    print("elememt not found")