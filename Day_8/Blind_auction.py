from art import logo
print(logo)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bid = {}
should_continue = True
while should_continue:
    print("Welcome to the Blind Auction!")
    name = input("What is your name? \n")
    price = int(input("How much would you like to bid ? $ \n"))
    bid[name] = price
    print("\n" * 100)
    more_bidders = input ("Are there any more bidders. Type yes or no: ")
    if more_bidders == "no":
        should_continue = False
        find_highest_bidder(bid)
    elif more_bidders == "yes":
        print("\n" * 100 )