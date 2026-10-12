## problem 5.1

import math
a = math.sqrt(44)
b = math.radians(90)
c = math.sin(math.radians(70))

print("a= ",a)
print("b= ",b)
print("c= ",c)

## Problem 5.2
##import requests  ##pip install requests
##a= requests.get("https://api.github.com/")
##print(a.json())


## problem 6.1
def increment():
    counter =0
    counter +=1
    print(counter)

increment()
increment()
increment()
increment()

## Problem 6.2

def multiply(a,b):
    '''
    Multiply two numbers
    Parameter:
    a(int or float : The First number)
    b(int or float : the Second number)
    Returns:
    int or float : The product of a and b
    '''
    return a*b

## Example 
print(multiply(5,3))
print(multiply(5.5,8))
help(multiply)