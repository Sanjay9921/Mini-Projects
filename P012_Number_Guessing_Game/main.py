from play_game import *

end_game = False
while not end_game:
    play_game()
    choice = input("Press 'y' to continue to the next game, 'n' to quit..").casefold()
    if choice=="n":
        print("Thank you for using our software!")
        end_game = True