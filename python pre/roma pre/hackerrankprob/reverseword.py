str = "hello this is roma here"
words = str.split()
print(words)
words = words[-1::-1]
print(words)
otp = ' '.join(words)
print(otp)