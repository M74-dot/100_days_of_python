auction_dict = {}

def find_highest_bidder(auction_dict):
    highest_bidder = 0
    for person in auction_dict:
        bid = auction_dict[person]
        if bid > highest_bidder:
            highest_bidder = bid
            winner = person
    return winner,highest_bidder
    

bidding_finish = False
while not bidding_finish:
    name = input("What's your name? ")
    bid_price = int(input("What is your bid? $"))

    auction_dict[name] = bid_price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finish = True
        winner, highest_bidder = find_highest_bidder(auction_dict)
        print(f"The winner is  {winner} with a bid of {highest_bidder}")
