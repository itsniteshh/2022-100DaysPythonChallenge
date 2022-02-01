#Write your code below this line 👇
def prime_checker(number):
    #function to check prime number
    is_prime = True
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                #the number is prime, triggers false if it is not prime num
                is_prime = False

        if is_prime:
            print(f"{number} is a a prime number")
        else:
            print(f"{number} is not a prime number")
    else:
        print(f"{number} is a not a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)




