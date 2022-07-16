# input: aaaaabbbbbrrrrrccczzz  opt: 5a1z

str1 = 'aaaaabbbbbrrrrrccczzz'

output = ""

char=str1[0]
count=0

for ch in str1:
    if ch==char:
        count+=1
   
    else:
        output = output+str(count)+char
        count=1
        char=ch
output = output+str(count)+char
print(output)


s = "a3b5c4r4"

otp = " "

for ch in s:
    if ch.isalpha():
        var = ch
    else :
        num = int(ch)
        otp=otp+(var*num)
print(otp)


