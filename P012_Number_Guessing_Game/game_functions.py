##Number Guessing Game
#All functions

def check_answer(guess:int, answer:int, turns:int)->int:
    """Compares the guess and the answer and returns the turns remaining"""

    if guess > answer:
        print("You guessed too high!")
        return turns-1
    elif guess < answer:
        print("You guessed too low!")
        return turns-1
    else:
        print("You guessed it right!")

def set_difficuty():
    """User can select if they wish to guess in 'easy' i.e., 10 turns or 'hard' i.e., 5 turns"""
    choice = input("Choose a difficulty: 'easy' or 'hard'").casefold()
    if choice=="easy":
        return 10
    else:
        return 5

def welcome_msg():
    print("Welcome to the Number Guessing Game!")
    print("Rules - guess the game before the turn ends")

