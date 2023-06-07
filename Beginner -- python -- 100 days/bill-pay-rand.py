# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


n = len(names)      # len will give length (size) of list
bill_payer = random.randint(0,(n-1))          #bug fixed n to n-1

print(f"Bill will be payed by {names[bill_payer]}.")

# there is a function called choice() that randomly choses a item from the list