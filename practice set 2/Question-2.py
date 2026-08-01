#match case
#number -1
num = int(input("Enter a numbers between 1 to 7: "))
match num: 
    case 1: 
        print("It's Friday")
    case 2: 
        print("It's Saturday")
    case 3: 
        print("It's Sunday")
    case 4: 
        print("It's Monday")
    case _:
        print("It's Tuesday Wednesday Thursday corresponding")

#number-2
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))

operation = input("Choose operation: ")
match operation : 
    case "+":
        print("a+b= ", a+b)
    case "-": 
        print("a-b= ", a-b)
    case "%":
        print("a%b= ", a%b)
    case "/": 
        print("a/b= ", a/b)
