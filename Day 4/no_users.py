usernames = []



if usernames:
    for names in usernames:
        if "admin" in names:
         print(f"\nHello {names}, would you like to see the status report of our website!\n")
        else:
            print(f"hello {names}, thank you for loggin in!")
else:
    print("we need to find some users for our website")
