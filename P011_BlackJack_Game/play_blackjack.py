from art import *
from blackjack import *

def play_game():
    #Display Logo
    print(logo)

    #List
    user_cards = []
    comp_cards = []

    #Game Over Variable
    game_over = False

    #Initialize two cards each for user and computer
    for i in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    #User plays first
    while not game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"User has {user_cards} and a score: {user_score}")
        print(f"Opponent's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_choice = input("Type 'y' to get another card, 'n' to pass...")
            if user_choice == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    #Computer plays next
    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    print(f"{'*'*10} FINAL HAND {'*'*10}")
    print(f"User has {user_cards} and a score: {user_score}")
    print(f"Computer has {comp_cards} and a score: {comp_score}")
    print(compare(user_score, comp_score))