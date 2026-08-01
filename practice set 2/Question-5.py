#Break Continue Pass Statements
#number 1
for i in range(0,11):
    print(i)
    if i ==7:
        break

#number 2
for i in range(0,20):
    if i ==10 or i ==12 or i ==14:
        continue 
    print(i)

#number 3
for i in range(0,20):
    if i==12:
        pass
    print(i)