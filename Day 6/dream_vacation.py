
dream_vacation = {}

is_active = True
while is_active:
    name = input("Enter ur name: ")
    place = input("Enter ur dream vacation? ")

    dream_vacation[name] = place

    another_poll = input("does anyone else wants to give another poll? ")

    if another_poll == "no":
        is_active = False 

print(dream_vacation)