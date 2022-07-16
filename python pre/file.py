

f = open("sample.doc", "r")
# data = f.read()
# data = f.read(11)
data = f.readline()
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)
data = f.readline()
print(data)
f.close()
