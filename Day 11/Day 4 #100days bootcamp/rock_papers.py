rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

games = [rock, paper, scissors]

#user guess
user_guess = int(input("Enter 0 for rock, 1 for paper and 2 for scissors: \n"))

if user_guess == 0:
    print(f"You chose: {games[0]}")
elif user_guess == 1:
    print(f"You chose: {games[1]}")
elif user_guess == 2:
    print(f"You chose: {games[2]}")


#for com guess
com = len(games)

com_guess = random.randint(0, com-1)

if com_guess == 0:
    print(f"Com chose: {games[0]}")
elif com_guess == 1:
    print(f"Com chose: {games[1]}")
elif com_guess == 2:
    print(f"Com chose: {games[2]}")



if user_guess == com_guess:
    print("Match drawn")
elif user_guess == 0  and com_guess == 2:
    print("User wins")
elif user_guess == 2  and com_guess == 1:
    print("User wins")
elif user_guess == 1  and com_guess == 0:
    print("User wins")
else:
    print("Com wins")

