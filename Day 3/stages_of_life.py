import random

person = random.randint(1, 100)

if person <=2:
    print("You're a baby")
elif person <= 13:
    print("You're a kid")
elif person <20:
    print("Your a teenager")
elif person <65:
    print("You're an adult now")
else:
    print("You're an elder")