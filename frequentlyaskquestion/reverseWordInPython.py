word = "hello this is roma here"

new_word=word.split()
print(new_word)

print(new_word[-1::-1])

reverse = new_word[-1::-1]

otp=' '.join(reverse)
print(otp)