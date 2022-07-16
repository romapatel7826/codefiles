s = input("enter yourstr:")
print(s[:])
print(s[0:4:1])
reversestr=(s[::-1])

if reversestr==s:
    print(" string is palindrome")
else:
    print("string is not a plaindrome")
