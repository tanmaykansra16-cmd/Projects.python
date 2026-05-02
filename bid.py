# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def highest_bidder(biding_dictionary):
    winner =""
    highest_bid =0
    for bidder in  biding_dictionary:
        bid_amount = biding_dictionary[bidder]
        if bid_amount> highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with bid amount {highest_bid}")
bid = {}

continue_bidding = True

while continue_bidding:

    name = input("What is your name?")
    price = (int(input("What is you biding amount? :$ ")))
    bid[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        continue_bidding = False
        highest_bidder(bid)
    elif should_continue == "yes":
        print("\n" * 20)




