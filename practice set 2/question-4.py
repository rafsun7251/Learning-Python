#while loop
#number 1
i = 0 
while i<10:
    i = i+1
    print(i)

#number 2
password = "5632" 
enter_password = input("Enter your password: ")
while(enter_password != password):
    enter_password = input("Wrong password please try again: ")

print("Successfully logged in")

#number 3
num = int(input("Enter a number: "))

print("Reverse Number: ",int(str(num)[::-1]))