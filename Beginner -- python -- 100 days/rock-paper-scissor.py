import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
while 1==1:
    player_input = int(input("Enter 0,1 and 2 for rock, paper, scissors respectively: "))

    comp = random.randint(0,2)

    if player_input == 0:
        if comp == 0:
            print(rock + "\n\n")
            print(rock + "\n\n")
            print("DRAW")
        elif comp == 1:
            print(rock + "\n\n")
            print(paper + "\n\n")
            print("COMPUTER WIN")
        else:
            print(rock + "\n\n")
            print(scissors + "\n\n")
            print("YOU WIN")

    elif player_input == 1:
        if comp == 1:
            print(paper + "\n\n")
            print(paper + "\n\n")
            print("DRAW")
        elif comp == 2:
            print(paper + "\n\n")
            print(scissors + "\n\n")
            print("COMPUTER WIN")
        else:
            print(paper + "\n\n")
            print(rock + "\n\n")
            print("YOU WIN")

    elif player_input == 2:
        if comp == 0:
            print(scissors + "\n\n")
            print(rock + "\n\n")
            print("COMPUTER WIN")
        elif comp == 1:
            print(scissors + "\n\n")
            print(paper + "\n\n")
            print("YOU WIN")
        else:
            print(scissors + "\n\n")
            print(scissors + "\n\n")
            print("DRAW")

    else:
        print("invalid input")







# if player_input == 0:
# elif player_input == 1:
# elif player_input == 2:
# else:
#     print("invalid input")
#
# if player_input == 0:
#     if comp == 0:
#         print(rock + "\n\n")
#         print(rock + "\n\n")
#         print("DRAW")
#

