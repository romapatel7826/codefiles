num = int(input("enter your number: \n"))

prime = True

for i in range(2, num):
    if(num % i == 0):
        prime = False
        break
if prime:
    print("number is prime")
else:
    print("number in not prime")
