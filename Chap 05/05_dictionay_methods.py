myDict = {
    "fast":"In a quick manner",
    "harry":"A coder",
    "marks": [1,2,5],
    "anotherdict":{'harry':'player'},
    1: 2
    }

print(list(myDict.keys()))
print(myDict.keys())
#print(type(myDict.keys()))-->type is dict keys

print(myDict.items())

print(myDict)
updateDict = {
    "lovish": "friend"
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("harry"))
print(myDict["harry"])

#wait let see when not present

print(myDict.get("harry2"))#it result none
print(myDict["harry2"])#it throw error thats why we use get key