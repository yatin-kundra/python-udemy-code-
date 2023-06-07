import random


# get cards
# sum show
# hit or stand
    # hit then give new cards
        # ckeck for black jack or 11 and 1 condition
# win check and computer turn
# his win and my turn

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]












def win(playerscore, dealerscore):
    if playerscore > 21 and dealerscore > 21:
        # print(f"you lose , your score {playerscore}")
        return "lose"


    if playerscore == 0:
        # print(f"you win with a black jack , your score {playerscore}  ")
        return "win bj"
    elif dealerscore == 0:
        # print(f"you lose pponent has a black jack , your score {playerscore}")
        return "lose"

    elif playerscore > dealerscore:
        # print(f"you win , your score {playerscore}")
        return "win"

    elif playerscore > 21:
        # print(f"you lose")
        return "win"

    elif playerscore == dealerscore:
        return "draw"

    elif dealerscore > 21:
        # print("you win")
        return "win"

    else:
        # print("you lose")
        return "lose"

















def playgame():


    def score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if sum(cards) > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        score = sum(cards)
        return score







    def getCards():
        for i in range(0,2):
           card = random.choice(cards)
           return card

    playerCards = []
    dealerCards = []



    for i in range(0,2):
        playerCards.append(getCards())
        dealerCards.append(getCards())
    print(f"player cards : {playerCards} , your score {score(playerCards)}")
    print(f"dealer cards : [{dealerCards[0]}, X] ")

    def Continue():
        next = input("do you wish to hit or stand: ").lower()
        if next == "hit":
            playerCards.append(getCards())
            print(f"player cards : {playerCards} player score : {score(playerCards)}")
            print(f"dealer cards : {dealerCards} dealer score : {score(dealerCards)}")



        elif next == "stand":
            print(f"player cards : {playerCards} player score : {score(playerCards)}")
            print(f"dealer cards : {dealerCards} dealer score : {score(dealerCards)}")
            return True
            # win(score(playerCards), score(dealerCards))

        else:
            print("Invalid input")


    gameOver = False
    while not gameOver:
        if score(playerCards) > 21 or score(playerCards) == 0:
            gameOver = True

        else:
            gameOver= Continue()
            # gameOver = False



    while score(dealerCards) != 0 and score(dealerCards) < 17:
        dealerCards.append(cards)
        print(f"player cards : {playerCards} player score : {score(playerCards)}")
        print(f"dealer cards : {dealerCards} dealer score : {score(dealerCards)}")
        print(win(score(playerCards), score(dealerCards)))

play = input("do you want to play again 'y' or 'n' : ").lower()
while play == "y":
    playgame()



