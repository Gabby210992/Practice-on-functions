fgimport string
from caesar_cipher_logo import logo
alphabet = list(string.ascii_lowercase)
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here is the {direction}d result: {end_text}")


print(logo)
play_again = True
while play_again:
    direction = input("Enter 'encode' or 'decode' to proceed: \n")
    if direction == "encode":
        text = input("Type your message to encrypt or decrypt: \n").lower()
        shift = int(input("Type the shift number: \n"))
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction) 
    elif direction == "decode":
        text = input("Type your message to encrypt or decrypt: \n").lower()
        shift = int(input("Type the shift number: \n"))
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    else:
        print ("I do not understand your input. Please enter a valid input.\n")
    do_you_want_to_continue = input("Do you still want to re-run the program? Type \"yes\" or \"no\" \n").lower()
    answer = True
    while answer:
        if do_you_want_to_continue == "no":
            answer = False
            play_again = False
        elif do_you_want_to_continue == "yes":
            answer = False
        else:
            do_you_want_to_continue = input(
                "I do not understand your input.Please enter a valid input? Type \"yes\" or \"no\" \n"
                ).lower()