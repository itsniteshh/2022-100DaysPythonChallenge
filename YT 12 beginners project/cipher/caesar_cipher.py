alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def cesar_cipher(direction, text, shift):
    #function to encrypt or decrypt code based on input
    cipher_code = ""
    if direction == "encode":
        for index, letters in enumerate(text):
            new_pos = alphabet.index(letters)
            pos = new_pos + shift
            new_code = alphabet[pos]
            cipher_code += new_code

    else:
        for index, letters in enumerate(text):
            new_pos = alphabet.index(letters)
            pos = new_pos - shift
            new_code = alphabet[pos]
            cipher_code += new_code

    print(f"The {direction} text is {cipher_code}")


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    another_try = input("Do you want to try again? type 'no' to exit: \n")

    if another_try == "no":
        break
    
    cesar_cipher(direction, text, shift)