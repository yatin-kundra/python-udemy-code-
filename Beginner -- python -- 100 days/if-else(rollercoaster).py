print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height < 120:    # this the condition over which the discision is made
  print("sorry you cannot ride this rollercoaster!")  # compiler will print this if the statement is true
else:
  print("Enjoy your ride.")   # compiler will print this if the statemt is false


#height < 120 doesnot include 120 to include 120 we will need to change < with <=