from art import logo

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
            
    return f"{num1} {symbol} {num2} = {answer}"

end_of_game = True
print(logo)

while end_of_game:
    num1 = float(input("\nEnter first number: \n"))
    num2 = float(input("\nEnter second number: \n"))
    symbol = input("\nEnter calculation type: \n'+' for addition, \n'-' for subtraction, \n'/' for division, \n'*' for multiplication \n")

    final_answer = doing_calculation(num1, num2, symbol)
    print(f"\nThe final answer is: '{final_answer}'\n")

    try_again = input("Do you want to play again? type 'no' to exit: \n")

    if try_again == "no":
        break
    else:
        pass

