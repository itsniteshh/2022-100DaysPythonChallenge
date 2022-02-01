from art import logo, vs
import random
from game_data import data


def guess1_information(random_guess1):
    #function to return a string about first guess  
    guess1_info = (f"Compare A: {random_guess1['name']}, a {random_guess1['description']}, from {random_guess1['country']}.")
    return guess1_info

def guess2_information(random_guess2):
    #function to return a string about second guess  
    guess2_info = (f"Against B: {random_guess2['name']}, a {random_guess2['description']}, from {random_guess2['country']}.")
    return guess2_info




def guess1_followers(random_guess1):
    #function to return just the followers of our first guess
    followers1 = random_guess2["follower_count"]
    return followers1

def guess2_followers(random_guess2):
    #function to return just the followers of our first guess
    followers2 = random_guess2["follower_count"]
    return followers2


def checking_bigger_value(random_guess1, random_guess2):
    #function to check  which follower count is bigger
    if random_guess1["follower_count"] > random_guess2["follower_count"]:
        return 0        
    else:
        return 1

def assigning_user_guess_to_num_for_checking(user_guess):
    #function to assign user guess to num format to check if user guessed right
    if user_guess == "A":
        return 0
    else:
        return 1

score = 0
random_guess1 = random.choice(data)
end_of_game = True


while end_of_game:

    random_guess2 = random.choice(data)
    #making sure if both values are diff
    if random_guess1 == random_guess2:
        random_guess2 = random.choice(data)
    guess1 = guess1_information(random_guess1)
    guess2 = guess2_information(random_guess2)

    #printing basic variables
    print(logo)
    print(guess1)
    print(vs)
    print(guess2)

    #taking user input
    user_guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()

    #checking for the winner and incrementing score 
    if assigning_user_guess_to_num_for_checking(user_guess) == checking_bigger_value(random_guess1, random_guess2):
        score += 1
        print(f"You're right! You earned {score} points")

    else:
        print("You're wrong! Game over")
        print(f"Final score is {score}")
        end_of_game = False

    #if user guesses correct answer-- using recursion to assign second value to first
    if assigning_user_guess_to_num_for_checking(user_guess) == checking_bigger_value(random_guess1, random_guess2):
        random_guess1 = random_guess2


print("\nThank you for playing our game! Hope to see you soon")

    
