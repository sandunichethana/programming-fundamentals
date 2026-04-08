units=int(input("enter units consumed"))
if units<=50:
    bill=(units*50)+1000
elif units<=100:
    bill=(50*50)+((units-50)*100)+1000
else:
    bill=(50*50)+(50*100)+((units-100)*150)+1000

print("the bill is",bill)
