import random
from urllib.parse import uses_fragment

#com will randomly generate a guess
## user will enter a guess in a forever while loop
## when the user guess matches com guess, user wins and loop stops
## loop stops also when user loses all her 3 lives


com_guess = random.randint(1, 100)
lives = 3
end_of_game = True

while end_of_game:
    user_guess = int(input("Enter a guess from 1 to 100: "))
    if user_guess == com_guess:
        print("You guessed the right number! Cingrats, you win")
        break
    elif user_guess > com_guess:
        print("Number too high!")
        lives -= 1
    elif user_guess < com_guess:
        print("Number too low!")
        lives -= 1
    if lives == 0:
        print(f"\nYou ran out of lives! You lose")
        break


