from art import *
from random import randint
from game_functions import *

def play_game():
    #Display Logo
    print(logo)

    #Display welcome message
    welcome_msg()

    print("I'm thinking a random number between 1 and 100...")
    answer = randint(1,100)

    #Comment the line below
    print(f"Psst...the answer is {answer}")

    #Number of turns for user
    #Easy=10
    #Hard=5
    turns = set_difficuty()

    guess = -1
    while guess != answer:
        print(f"You have {turns} turns remaining...")

        guess = int(input("Make a guess (1-100): "))
        turns = check_answer(guess, answer, turns)

        print()

        if turns==0:
            print("You have run out of guesses! You lose!")
            return
        elif guess!=answer:
            print("Guess again!")

        print()

    print(f"I guessed {answer}")







