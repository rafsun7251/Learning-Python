#mehtods
text = "hello world"
a= len(text) # len- lenth of function 
print("Text lenth: ",a)
print(text.upper()) # all letter  will be upper class
print(text.lower())  #all letter will be lower class
print(text.capitalize())  # first letter line will be upper
print(text.title())  # first letter  of all  word will be upper

#whitespace

print(text.strip())  
print(text.lstrip()) #left 
print(text.rstrip())  #right

#finding & replacing 
print(text.find("w")) # find word or letter
print(text.replace("world", "Bangladesh"))

# splitting & joining
txt = "Apple, Banana, Orange"
fruits = txt.split(",") #output: ['Apple' , 'Banana' , 'Orange']
print(fruits)  
new_txt = "-".join(fruits)
print(new_txt)  #Aoutput: pple- Banana- orange