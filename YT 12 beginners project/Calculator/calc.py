
def doing_calculation(num1, num2, symbol):
    """A function that does our calculation part for the calc appp"""
    if symbol == '+':
        answer = num1 + num2
        
    elif symbol == '-':
        answer = num1 - num2

    elif symbol == '/':
        answer = num1 / num2

    elif symbol == '*':
        answer = num1 * num2

    return answer

end_of_game = True
num1 = float(input("\nEnter first number: \n"))

while end_of_game:
    symbol = input("\nEnter calculation type: \n'+' for addition, \n'-' for subtraction, \n'/' for division, \n'*' for multiplication \n")
    num2 = float(input("\nEnter next number: \n"))

    ans = doing_calculation(num1, num2, symbol)
    print(f"{num1} {symbol} {num2} = {ans}")

    try_again = input("Do you want to use calc again? type 'no' to exit: \n")
#the below is recursive function option, wherein we assign the total of first calc to the first sum
    if try_again == "yes":
        num1 = ans
    else:
        end_of_game = False

