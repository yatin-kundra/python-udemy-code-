#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for letter in letter_random:
#     print(letter)

password = " "
for l in range(0,nr_letters):
    letter_random = random.randint(0, 25)
    # print(ltterse[letter_random])
    password += letters[letter_random]
for s in range(0,nr_symbols):
    symbol_random = random.randint(0, 8)
    # print(symbols[symbol_random])
    password += symbols[symbol_random]

for n in range(0,nr_numbers):
    number_random = random.randint(0,9)
    # print(symbols[symbol_random])
    password += numbers[number_random]

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# new_pass = password.split()
# for new in range(0,nr_numbers + nr_symbols + nr_letters):
#     Pass = new_pass[random.randint(0,(nr_numbers + nr_symbols + nr_letters))]
#     print(Pass)






#   IS GENERATING WRONG PASS AS IN NOT SAME AS THE EASY PASS

# Pass = " "
# for new in range(0,len(password)):
#     new_pass = random.choice(password)
#     Pass += new_pass
# print(Pass)
#


# password1 = []
newpassword = ""
for p in range(0, (len(password)-1)):
    # password1 += password.strip(" ")
    list1 = list(password.strip(" "))   # strip function is being used to change string into list.
    # newpassword += random.choice(list1)
    random_index = random.randint(0,(len(password)-1))
    newpassword += list1[random_index]
print(list1)
print(newpassword)

# print(random.choice(password1))

