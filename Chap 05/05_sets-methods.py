s=set()
print(s)

s.add(3)
s.add(5)
s.add(55)
#s.add(5,7)>>>wrongg
s.add((4,5,5,6))
print(s)

print(len(s))

s.remove(5)
#s.remove(445)-->>throw error as not present in set
print(s)

print(s.pop())

print(s.union({4,5}))
print(s.intersection({3,4,5}))