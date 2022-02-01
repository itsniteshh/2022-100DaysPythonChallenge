from art import logo
import random
print(logo)


def remaining_lives(difficulty, life):
    """a function to use lives global var and change its value depending on difficulty"""
    global lives

    if difficulty == "hard":
        lives = 3
    else:
        lives = 5      
    return lives

lives = 0
end_of_game = True
random_guess = random.randint(1, 100)
print("\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
print(f"guessed word is: {random_guess}")
remaining_lives(difficulty, life = lives)


while end_of_game:
    guess = int(input("\nMake a guess: \n"))

    if guess == random_guess:
        print("\nYou win 😎")
        end_of_game = False

    elif guess < random_guess:
        print("Too low!")
        lives -= 1
        print(f"you have {lives} attempt remaining")

    else:
        print("Too High!")
        lives -= 1
        print(f"you have {lives} attempt remaining")
    

    if lives == 0: 
        print("You ran out of lives. You lose 😤")
        break


print("Thank you for playing our game!")