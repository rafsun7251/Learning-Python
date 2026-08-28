#default arguments
def add(a,b,c,plus=2): #plus=2 is default arguments
    return a+b-c   #a,b,c = parameter
d= add(3,4,1)       #3,4,1= arguments
print(d)

def greet(name="Rafsun"):
    return f"Hello , {name}!"
print(greet())

#keywords arguments

def student(name, age):
    print(f"Name : {name}, Age: {age}")
student(name= "Rafsun", age=20)
        