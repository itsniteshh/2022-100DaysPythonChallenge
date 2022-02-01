import random

our_guess = 4
end_of_game = True


while end_of_game:
    # while loop to make com guess diff numbers 
    
    com_guess = random.randint(1, 10)
    print(f"Com guessed {com_guess}")
    if com_guess < our_guess:
        print("Value to less! Try again Com")
    elif com_guess > our_guess:
        print("Value too big! Try again com")
    else:
        print("Yeah! Com wins")
        end_of_game = False

