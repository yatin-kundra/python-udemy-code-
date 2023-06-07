# from replit import clear
from ART import logo

auction = {}

def heightstBidder(biddingRecord):
    heighestBid = 0
    for bidder in auction:
        bidAmount = auction[bidder]
        if heighestBid < bidAmount:
            heighestBid = bidAmount
            winner = bidder
    print(f"the heighest bid is of {bidder} with amount of {heighestBid} ")



# HINT: You can call clear() to clear the output in the console.
Continue = True
while Continue:         # YOU CAN NOT MAKE IT Continue = True

    print(logo)
    name = input("enter your name: ")
    bidAmount = int(input("enter your biding amount: "))

    auction[name] = bidAmount

    YN = input("do you wish to continue yes(y) or no(n)").lower()
    if YN != "y":
        Continue = False
        heightstBidder(auction)

