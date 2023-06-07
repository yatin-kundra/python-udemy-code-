import random
list_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

deal_computer = []
deal_player = []

player_points = 0
dealer_points = 0
def score(points):
    player_points = sum(points)
    dealer_points = sum(points)


def win():
    if score(player_points) > 21 and score(dealer_points):
        deal_player.remove(11)
        deal_player.append(1)
        deal_computer.remove(11)
        deal_computer.append(1)



    elif score() == 21 and len(deal_player) == 2  and len(deal_computer) == 2:
        print("Blac Jack")


        if player_points <= 21 and dealer_points <= 21:
          if player_points > dealer_points:
            print("you win!")
          # elif dealer_points > player_points:
          #     print("you lose")
          else:
            deal_computer.append(random.choice(list_of_cards))
            print(f"Dealer : {deal_computer}")
            print(f"player : {deal_player}")
            win()
        elif player_points > 12 :
            print("you lose")
        elif dealer_points > 21:
            print("you win!!")

    else:
        print()


def deal():
    for i in range(0,2):
      deal_computer.append(random.choice(list_of_cards))
      deal_player.append(random.choice(list_of_cards))
    # deal_computer[1] = "x"
    print(f"Dealer : [{deal_computer[0]}, X]")
    print(f"player : {deal_player}")

    next = input("do you wish to hit or stand ? ").lower()
    if next == "hit":
        deal_player.append(random.choice(list_of_cards))
        # deal_computer[1]
        print(f"Dealer : {deal_computer}")
        print(f"player : {deal_player}")
        win()
    elif next == "stand":
        print(f"Dealer : {deal_computer}")
        print(f"player : {deal_player}")
        win()

    print(player_points)

#
# def win():
#     win = True
#     if score() > 21:
#         win = False
#     else:
#





deal()
