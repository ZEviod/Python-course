'''n=4
product =1
for i in range(n):
    product = product*(i+1)
print(product)'''

def fact_iter(n):
    product =1
    for i in range(n):
        product = product*(i+1)
    return product

def fact_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n*fact_recursive(n-1)

print(fact_iter(5))
f = fact_recursive(4)
print(f)