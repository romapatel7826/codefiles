def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def si(p, r, t):

    return (p*r*t)/100

def ci(P, R, T):
    return P * pow((1+R/100),T)

def sqr(num):
    return  num**2


print(si(50,20,2))
print(sqr(5))