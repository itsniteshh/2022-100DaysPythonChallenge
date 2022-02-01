active = True

while active:
    print("Enter topping for your pizza")
    print("Type 'quit' to exit")
    pizza = input()

    if pizza == "quit":
        break
    else:
        print(f"we weill get you your {pizza} PIZZA\n")

print("yOUR PIZZA IS ready")