# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")   #  23
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

vertical = int(position[0]) # 2
horizontal = int(position[1])    #3
selected_row = map[horizontal - 1]
selected_row[vertical - 1] = "x"








#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")