class Employee:
    company = "Google"
    salary = 10000

ram = Employee()
raju = Employee()

#creating instance attribute salary for both objects
#ram.salary = 3000
#raju.salary = 4200


ram.salary = 3000
print(ram.salary)
print(raju.salary)


#print(raju.address)-->this is throwing error as not present in instance as well class