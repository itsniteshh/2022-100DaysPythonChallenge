# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_cost = 0

if size == "S":
  total_cost += 15
  if add_pepperoni == "Y":
    total_cost += 2
    if extra_cheese == "Y":
      total_cost += 1
elif size == "M":
  total_cost += 20
  if add_pepperoni == "Y":
    total_cost += 3
    if extra_cheese == "Y":
      total_cost += 1
else:
  total_cost += 25
  if add_pepperoni == "Y":
    total_cost += 3
    if extra_cheese == "Y":
      total_cost += 1

print(f"You're total bill is {total_cost}")
print("Thank you for ordering with us")



