num = int(input("enter your  num: "))
fact = 1

if num<0:
    print("factorial is does not exist for negative num")
elif num == 0:
    print("the factorial of 0 is 1")
else:
   for i in range(1,num+1):
     fact = fact*i
print("fact", num, "is", fact)
