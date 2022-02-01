import random

#splitting string to a list
names = input("Enter the names of ppl followed by comma: \n")
name = names.split(",")

for words in range(len(name)):
    payer = random.randint(0, words) #for choosing randomly not using choice function

'''
payer = random.choice(name)
'''

print(f"The bill will be payed by {name[payer]}")
