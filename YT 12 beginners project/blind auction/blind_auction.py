def highest_bidder(blind_auction):
    #function to get the highest bidder's name and amount from the dict
    bidder = ""
    amount = 0

    for k, v in blind_auction.items():
        if amount < v:
            amount = v
            bidder = k
        
        print(f"The winner of our game with highest bid is '{bidder}' with '{amount}' bid")



end_of_the_game = True
blind_auction = {}

while end_of_the_game:
    name = input("\nEnter your name: ").title()
    bid_amount = int(input("Enter bid amount: "))
    try_again = input("Do you want to try again? type 'no' to exit: \n").lower()

    blind_auction[name] = bid_amount

    if try_again == "yes":
        pass
    else:
        end_of_the_game = False

print(blind_auction)