def sum(a,b):
    ## a and b are local variables
    ## can access inside function
    c=a+b 
    z=3 
    return c
z=5 ##Global variable
print(sum(8,9))
print("Z =",z)
