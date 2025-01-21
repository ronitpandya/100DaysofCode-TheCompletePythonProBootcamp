# TODO-1: Ask the user for input
import art
auction = {}
auctionlive = True
print(art.logo)
# auction[input("Please write your name")] = input("give your buying price")

def find_highest_bidder(auction):
    winner = ""
    highest_bid = 0
    for bidder in auction:
        if auction[bidder] > highest_bid:
            highest_bid = auction[bidder]
            winner = bidder
    print(f"Highest bidder is {winner} bidding amount is ${highest_bid}")




while auctionlive:
    user_name = input("Please write your name")
    price = int(input("give your buying price"))
    auction[user_name] = price
    yesorno = input("is there another bid? type yes or no").lower()
    if yesorno == "no":
        find_highest_bidder(auction)
        auctionlive = False
    else:
        print("\n" * 100)






# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

