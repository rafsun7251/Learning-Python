''''
Fibonacci  Series

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) +  fib(1)
fib(3) = fib(1) + fib(2)
fib(4) = fib(2) + fib(3)
fib(n) = fib(n-2) + fib(n-1) 

'''
def fib(n): 
    #Base case 
    if ( n == 0 or n ==1):
        return n
    return fib(n-2) + fib(n-1) 
print("6 = " ,fib(6))
print("10 = ", fib(10))
print("12 = ", fib(12))