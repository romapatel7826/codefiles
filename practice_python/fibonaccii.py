# #by using for loop

# def fibonacci(n):
#     a, b = 0, 1
#     if n==1:
#       print(a)
#     else:
#         print(a)
#         print(b)

#     for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#         print(c)

# fibonacci(50)


# fibonacci using recursion method


def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))
n=10 

if n<=0:
    print("invalid")
else:
    for i in range(n):
        print(fibo(i))