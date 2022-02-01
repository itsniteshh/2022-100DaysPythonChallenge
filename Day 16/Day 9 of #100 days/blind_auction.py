#from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
#clear()

end_of_game = True
print(logo)
blind_auction = {}
count = 1

def highest_bidder(blind_auction):
    #function to compare highest bidder 
    highest_value = 0
    bidder = ""
    for k, v in blind_auction.items():
        if highest_value < v:
            highest_value = v
            bidder = k
    
    print(f"The highest bidder for our auction game is {bidder} with {highest_value}")


while end_of_game:
    name = input("Enter your name: ").title()
    bid_price = int(input("Enter your bid price: "))
    another_try = input("Do you want to try again? type 'no' to exit: \n").lower()

    blind_auction[name] = bid_price

    if another_try == "yes":
        pass
    else:
        end_of_game = False

highest_bidder(blind_auction)




