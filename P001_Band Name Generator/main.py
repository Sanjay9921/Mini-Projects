#Functions
def welcome_msg():
    print("Hello! Welcome to the Band Name Generator!")


def ask_questions():
    city = input("Which city did you grow up in? ")
    pet = input("What is the name of your pet? ")

    return (city, pet)


def band_generator():
    welcome_msg()

    city, pet = ask_questions()

    band_name = city + " " + pet

    return band_name

while True:
    choice = input("Do you wish to play the game? Press 'Y' to continue, 'N' to quit...").casefold()
    if choice=="y":
        band_name = band_generator()
        print(f"Your band name is: {band_name}!")
    else:
        print("Thank you for playing the Band Generator Game!")
        break