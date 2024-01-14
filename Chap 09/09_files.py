#open to read a file
#f = open("sample.txt","r")  -->> by default mode is "r"
f = open("sample.txt",)
data = f.read()
#data = f.read(5) #reads first five characters from the file
print(data)
f.close