# get a nubmer betweeen 1 to 100
# make a loop to ask for easy and haed level
# make a function that takes input and check for the game
# you need to check if number matches if not then according to lives ask the user to guess again


import random
n=0


level = input("you want to play 'easy' or 'hard' ?").lower()
guess = int(input("entre your guess: "))
def guess(number):
    random_mun = random.randint(1,100)
    if level == "easy":
        n == 11
    elif level == "hard":
        n==6
    for i in range(0,n):
        if number > random_mun:
            print("Too heigh")
        elif number == random_mun:
            print("you have guessed the number")
        else:
            print("Too low")


guess(guess)


# playAgain = 1
# while playAgain:
#
#     con =  input("do you want to play again? 'y' or 'n' : ").lower()
#     if con == "y":
#          guess(guess)
#
#     elif con == "n":
#          playAgain = 0
#          print("game over!!!")
#
# guess(guess)
#


