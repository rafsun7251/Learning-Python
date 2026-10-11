## Problem 1.1
def greet():
    print("Hello! Python Learner")

greet()


## Problem 1.2
def square(x):
    return x*x

print(str(3) + "*" + str(3) + "=" + str(square(3)))
print(str(5) + "*" + str(5) + " = " + str(square(5)))
print(str(25) + "*" + str(25) + " = " + str(square(25)))


## Problem 2.1
def full_name(first, middle, last):
    return f"{first} {middle} {last}"

print(full_name("Full Name: " ,"Golam " , "Rafsun"))

def full_name(first, last):
    return f"{first} {last}"

print(full_name("Golam " , "Rafsun"))

## problem 2.2
def calculate_area(length , width=12):
    return(length * width)

print(F"This area is reactangle {calculate_area(12,19)}")
print((calculate_area(12)))

## Problem 3.1

add = lambda a,b: a+b 

print(add(3,7))

## Problem 3.2
square = lambda x: x*x 
list1 = [1,2,3,4,5]
list2 = [5,5,9,4,3] 
list3 = [7,9,3,1,1]
list4 = [77,55,997,334]
list5 = [4569,4456,47,566]

print(list(map(square, list1)))
print(list(map(square, list2)))
print(list(map(square, list3)))
print(list(map(square, list4)))
print(list(map(square, list5)))

## Problem 4.1
def factorial(n):
    if n==0 or n==1:
        return 1
    return factorial(n-1)*n
print(factorial(2))
print(factorial(4))
print(factorial(8))

## Problem 4.2
def sum_of_digits(n):
    if n==0 :
        return 0
    return n%10 + sum_of_digits(n//10)

##sum of digits 7532 is same as: 
## 2 (last digits)+ sum of digits 753

print(sum_of_digits(52))
print(sum_of_digits(655544))
