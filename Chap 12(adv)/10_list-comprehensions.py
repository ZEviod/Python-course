a = [3, 4, 5, 756, 42, 5, 8, 6445, 45, 63]
#b = []
#for item in a:
#    if item%2==0:
#        b.append(item)
#print(b)

#shortcut to write same
b = [i for i in a if i%2==0]
print(b)

t = [1,2,3,4,2,32,1]
s = {i for i in t}
print(s)