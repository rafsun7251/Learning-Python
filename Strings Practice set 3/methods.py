#number -1
text = " I love python programming "


print("Left side whhitespace: ",text.lstrip()) # only left side 
print("Right side whiitespace: ",text.rstrip())  #only right side
print("Both side whitespace: ",text.strip())  #both side 

print("Title: ", text.title())  #convert to title case
print("Total o count: ", text.count("o")) #count

#number -2
str = "123abc"
print("Is alphabetics: ",str.isalpha())  #check only words
print("Is all digit: ",str.isdigit()) # check only number
print("Is word and number only: ",str.isalnum())  #check A-z and 0-9 means word and number
print("Is have any space, tab or newline: ",str.isspace())  # check space, tab,newline