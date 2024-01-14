class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"
    salary = 1000
    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmers")

    def takeBreath(self):
        print("I am a Programmer so I am breathing++...")

p = Person()
p.takeBreath()
print(p.country)
#print(p.company)-->throw error as person ki company nhi hai

e = Employee()
e.takeBreath()
print(e.company)
print(e.country)

pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)