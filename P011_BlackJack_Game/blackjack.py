##Black Jack Game
#Libraries
import random

#global variables
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

#All functions
def deal_card():
    """Returns a random card from the deck"""
    return random.choice(cards)

def calculate_score(cards:list)->int:
    """Takes a list of cards and returns the score calculated"""

    #BlackJack (Win!)
    if sum(cards) == 21 and len(cards)==2:
        return 0

    #Condition:
    #If score>21
    #And if Ace(11) is found
    #Replace it with 11 and then return the sum
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score:int, comp_score:int)->str:
    """Compares the user's and computer's scores"""

    if user_score > 21 and comp_score > 21:
        return "You went over, you lose!"
    elif user_score > 21:
        return "You went over, you lose!"
    elif comp_score > 21:
        return "Opponent went over, you win!"

    if user_score==comp_score:
        return "Draw!"
    elif comp_score == 0: #BlackJack
        return "You lose! Opponent has Blackjack!"
    elif user_score == 0: #Blackjack
        return "You win with a Blackjack!"
    elif user_score > comp_score:
        return "You win! You have a higher score than opponent!"
    else:
        return "You lose! You have a lower score than opponent!"
