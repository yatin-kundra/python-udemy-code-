#lists are data structure ,i.e way of storitg and organising data
# we store data using variables
# eg we have to store names of all the states in india and its not a good idea to crat
# 29 variables to store them, they have a connection between them and can be stored in alist
# lists are basicaly arrays in c
# lists can be used if you want order of some kind
fruits = ["mango","apple","peach"]
# lists have index
print(fruits[0])


fruits[2] = "grapes"

print(fruits)

# if we want to add something to list then we use functon called append\

fruits.append("cherry")

print(fruits)

# you can use extend function to add more than one item, like a whole another list at the end of
# the previous list.

fruits.extend(["kivi","pear","fig"])
print(fruits)

# you can go to pyth0n.org to  the documentation and try out more functions. no need to memorize everything . we have google


#split function when you need ot get a lita a as an input
#used in bill-pay-random program