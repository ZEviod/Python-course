def percent(marks):
    p = ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p 
#can also use -->> return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100

marks1 = [45,78,86,77]
percentage1 = percent(marks1)

marks2 = [88,45,23,97]
percentage2 = percent(marks2)\

print(percentage1, percentage2)