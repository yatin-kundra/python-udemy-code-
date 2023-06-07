import random
from art import logo
print(logo)
randomInt = random.randint(1,100)
#print(randomInt)   #to ceck if code if working or not
def no():
    """as for input to guess the nunber"""
    guess = int(input("enter your guessed number: "))
    return guess
level = input("enter the level you wish to play 'easy' 'hard' : ")

def game():
    """plays the game of guessing the number"""
    n = 0
    if level == "easy":
        n = 10
    elif level == "hard":
        n = 5
    for i in range(0 ,n):
        numbers = no()

        if numbers > randomInt:
            print("Too heigh")
        elif numbers < randomInt:
            print("Too low")
        elif i > n:
            print("you lose!!")

        else:
            print("you have guessed the number!!")
            break



game()


playAgain = 1

while playAgain:
    again =  input("do you want to play again ? 'y' or 'n' : ")
    if again == "y":
        game()
        playAgain = 1
    elif again == "n":
        print("thank you for playing!!!")
        playAgain = 0
