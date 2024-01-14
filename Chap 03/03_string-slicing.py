greeting = 'gm biro '
nam = "superdon"
#print(type(nam))
#print(greeting+nam)-->it also works
#c=greeting+nam
#print(c)

print(nam[4])#-->that number of letter print
#also nam[4]=a does not change that letter

#counting start from 0

print(nam[1:3])  #--> in this  1 2 hee print hongee
tut = nam[1:5]
print(tut)


print(nam[:3])#-->is same as nam[0:3]
print(nam[1:])#--> is same as nam[1:8] #7th is last letter so thats why 8
print(nam[0:8])

print(nam[-4:-1])#this is same as nam[4:7]

d = nam[0:8:2]
e = nam[0:8:3]
print(d)
print(e)