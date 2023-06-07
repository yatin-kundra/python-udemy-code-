#i dont know if its right
# her's 2,3 is diffrent and mine is diffrent , mine is 2nd row and 3rd column

# 🚨 Don't change the code below
row1 = ["1️","2️","3️"]
row2 = ["4️","5️","6️"]
row3 = ["7️","8️","9️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?Enter positons , seprated ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

pos = position.split(",")
if int(pos[0]) <=3 and int(pos[1]) <= 3:

    map[int(pos[0])-1][int(pos[1])-1] = "X"
    print(map[int(pos[0])-1][int(pos[1])-1])
    print(f"{row1}\n{row2}\n{row3}")


else:
    print("invalid input")


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
#print(map)