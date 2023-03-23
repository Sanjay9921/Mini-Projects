#Import Libraries
from art import *
from letters import *

#Display Logo
print(logo)

#Caesar Cipher Code
def caeser_cipher(str, shift, direction):
    result = ""
    if direction=="decode":
        shift *= -1

    for char in str:
        if char in alphabet:
            i = (ord(char)%97+shift)%26
            result += alphabet[i]
        else:
            result += str(char)

    return result

#While loop
end_of_display = False
while not end_of_display:
    direction = input("Enter 'encode' or 'decode'...")
    str = input(f"Enter text to {direction}").lower()
    shift = int(input("Enter shift amount..."))

    result = caeser_cipher(str, shift, direction)
    print(f"{str} > {direction} > {result}")

    choice = input("Continue playing? Enter 'Y' or 'N'...").lower()
    if choice=="n":
        print("Thank you for playing!")
        end_of_display = True