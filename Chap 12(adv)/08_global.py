a = 54 #global variable
def func1():
    global a #start using global variable (a)
    print(f"Print statement: {a}")
    a = 8 #local variable
    print(f"Print statement: {a}")

func1()
print(f"Print statement: {a}")