n = 3
for i in range(3):
    print(" " * (n-i-1), end="")#isse new line nhi hoga space nhi bdega
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))