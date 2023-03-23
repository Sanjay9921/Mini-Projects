from play_blackjack import *

end_of_game = False
while not end_of_game:
    play_game()
    choice = input("Do you wish to play another game? 'y' or 'n'").casefold()
    if choice=="n":
        print("Thank you for playing Blackjack! Do not get addicted to gambling! ")
        end_of_game = True