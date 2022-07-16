max = int(input("enter your number:\n"))

odd_num = []

for i in range(1, max):
    if i%2 == 1:
        odd_num.append(i)
print("odd_num: ", odd_num)