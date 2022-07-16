# dictonery is a key value pairs

myDict = {
    "name" : "roma a coder",
    "marks" : "[1, 3,  4, 8]",
    "anotherdict" : {'roma':'coder'},
    1:2
}
print(myDict['name'])
print(myDict['marks'])
print(myDict['anotherdict']["roma"])
print(list(myDict.keys()))
print(myDict.values())
print(myDict.items()) # print (key, value) pairs

updateDict = {
    "riya" : "python developer",
    "seema" : "my best friend",
    "name" : "roma is a softwere developer"
     
}

myDict.update(updateDict)
print(myDict)

print(myDict.get("name2")) # return nome
print(myDict["name2"]) # throws error