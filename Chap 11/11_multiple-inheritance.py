class Employee:
    company = "Visa"
    eCode = 1202

    def upgradeLevel(self):
        self.level = self.level+1

class Freelancer:
    company = "Fiverr"
    level = 0


class Programmer(Employee,Freelancer):#as Employee is written first that's why it print company visa
    #if we write Freelancer first then company will be Fiverr
    name = "Rohit"

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)