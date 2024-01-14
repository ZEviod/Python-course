class Employee:
    company = "Google"

    def showDetails(Self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"

    def getLang(self):
        print(f"The language is {self.language}")

    def showDetails(Self): 
        print("This is an programmer") 

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)