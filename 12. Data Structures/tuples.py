## A tuple is a collection of multiple item written inside parenthesis 
##$ Reason why use Tuple 1. Can multiple value store 2. To protect data modification, can't change data 
## 3. Use less mnemeory  4. Fixed data store 

a = ("Rahim", 3,1)
b =(4) 
print(a)
print(a[2])  
print(b)

## Unpacking Tuple
tuple = (3,2,1)
a,b,c = tuple 
print(a,b,c)  ## 3,2,1 declared as a,b,c

## Tuple Method 

tu = (3,1,55,665.33,34,55,5343,444,55,52,55)

print(tu.count(55)) ## it will check 55 what time in tuple 
print(tu.index(55)) ## index number