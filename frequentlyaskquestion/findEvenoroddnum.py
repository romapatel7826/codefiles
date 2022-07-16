# num = int(input("enter number: "))


# if num%2==0:
#     print("number is even ")
# else:
#     print("number in odd")


list = [2,3,4,5,6,7,8,9,10]

# sq = []

# for num in list:
#     sq.append(num*num)
# print(sq)

print([num*num for num in list if num%2==0 if num%3==0])


