import re

str = "welcome@@topython**programming@!!^@$"

regex=re.compile('[!@_#$%^&*()}{~<>?|\:]')

if(regex.search(str) == None):
    print("No special character presence in the string")
else:
    print("it contains special character")
    