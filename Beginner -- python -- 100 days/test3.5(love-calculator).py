# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()
L = name1.count("l") + name2.count("l")
O = name1.count("o") + name2.count("o")
V = name1.count("v") + name2.count("v")
E = name1.count("e") + name2.count("e")
T = name1.count("t") + name2.count("t")
R = name1.count("r") + name2.count("r")
U = name1.count("u") + name2.count("u")

digit1 = T+R+U+E

digit2 = L+O+V+E

love_score = int(str(digit1) + str(digit2))
if love_score > 1010:
    print("100%")
else:
    print(f"{love_score}%")

if love_score < 10 or love_score > 90:              # you can use logical operates on int data type
    if love_score > 100:
        print(f"Your love score is 100.")
    else:
        print(f"Your love score is {love_score}.You are like coke and menthos.")
elif love_score < 30:
    print("find someone else😂")

else:
    print("you are great together.")