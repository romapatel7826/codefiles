

# f = open("tests.doc", "a")
# f.write("hello this is roma here")
# f.close()

f = open("tests.doc", "r")
a = f.read()
print(a)

f = open("tests.doc", "w")
a = f.write("roma")
print(a)