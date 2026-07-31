#break loops

for i in range (0,20):
    print(i)
    if i==12 :   #cancel the execution this loop now
        break 

#continue loop

for i in range (0,20):
    if i==11:
        continue   #continue the loop for the next iteration here 
    print(i) 

#pass loop 
for i in range(0,20):
    if i ==3: 
        pass
    print(i)  