#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to 'Code with Nitesh Cafe'")

bill = float(input("How much is the bill amount: "))
persons = int(input("How many of you are present: "))
tip = int(input("How much tip do you want to give our staff: anything between 5 to 15%\n"))

total_tip = tip / 100
bill_calc = (bill  + total_tip) / persons

#final bill
print(f"Every person should pay: {round(bill_calc)}")
