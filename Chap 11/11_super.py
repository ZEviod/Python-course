class Person:
    country = "India"
    def __init__(self):
        print("Initializing person\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing employee\n")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        #super().__init__()
        print("Initializing programmer\n")

    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer so I am breathing++...")

#p = Person()
#p.takeBreath()

#e = Employee()
#e.takeBreath()

pr = Programmer()
#pr.takeBreath()