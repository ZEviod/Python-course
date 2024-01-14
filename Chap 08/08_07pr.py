def remove_and_strip(string,word):
    newstr = string.replace(word,"")
    return newstr.strip

this ="   Harry is a good coder   "
n = remove_and_strip(this, "Harry")
print(n)
#print(this)
#print(this.strip())