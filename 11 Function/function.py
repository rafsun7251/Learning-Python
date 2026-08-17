a = 2 
b =3
c= 10
average1 = (a+b+c)/2
total1 = (a-b-c)

print("Average: " ,average1)
print("Total: ", total1)

## Function starts with #def in python

def average2(a,b,c):
    d= (a+b+c)/2
    print("d: ", d)
    return d 
o1 = average2(2,3,5)
o2 = average2(3,6,9)
print("o1: ", o1)
print("o2: ", o2)