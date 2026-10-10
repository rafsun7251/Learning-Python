def sum(a,b):
    print("Z=0 will call ")
    c= a+b
    global z ## modify global z
    z=0
    return c

z=8
print(sum(3,4))
print("Z=",z)