# creat flow charts cause that helps with the logic and once the logic is done the all these is left is to write the code


# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Is a leap year")
    else:
      print("not a leap year")
  else:
    print("Is a leap year")
else:
  print("Not a leap year")

