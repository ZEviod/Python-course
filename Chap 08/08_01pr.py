def max(n1,n2,n3):
    if(n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3

m = max(3,5,56)
print("The value of maximum number is "+ str(m))
