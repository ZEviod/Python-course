class Employee:
    company = "Google"
    salary = 10000

ram = Employee()
raju = Employee()

ram.salary = 3000
raju.salary = 4200

print(ram.company)
print(raju.company)

Employee.company = "YouTube" #class attribute changed
print(ram.company)
print(raju.company)

print(ram.salary)
print(raju.salary)