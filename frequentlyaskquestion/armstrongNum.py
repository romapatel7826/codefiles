number  = int(input("enter number "))
order = len(str(number))
sum = 0

number_copy = number

while number>0:
    digit = number%10
    sum += digit ** order
    number = number//10

if (sum==number_copy):
    print("number is armstrong")
else:
    print("number is not armstrong")