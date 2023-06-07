# type casting is convertion of one type to another

# char_len = len(input(enter your name: ))
#
# ptint("ength of your name is"+ char_len +"character")       # this will give us error as we can't add int to char

# correct way to do this is using a function called "type"

# type tells you which is the type of the data stored in a variable , and we can then use functions like str to convert
# any given data type to strign.

char_len = len(input("enter your name: "))
type (char_len)
str_len = str(char_len)
print("ength of your name is"+ " "+ str_len +" character")


a =  str(123)

print(type(a))      # converting int to strirg


b = float(65442.5644)       # int to float
print(345 + b)

print(465 + 154)            # sinmple to int being added

print(str(6446) + str(81160))           #two strings concatinated