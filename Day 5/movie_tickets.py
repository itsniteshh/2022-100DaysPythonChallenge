while True:
    age = input("Enter ur age. Type 'quit' to exit \n")

    if age == "quit":
        break
    elif int(age) < 3:
        print("Enjoy lad! Your ticket is free")
    elif int(age) < 12:
        print("Your ticket is $10")
    elif int(age) > 12:
        print("Your ticket will cost $15")
    

print("Welcome to our theater")