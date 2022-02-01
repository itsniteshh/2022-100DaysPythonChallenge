guess = int(input("Enter a num of your choice? "))

if guess % 10 == 0:
    print(f"{guess} is a multiple of 10")
else:
    print(f"{guess} is not a multiple of 10")