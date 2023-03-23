import random

is_playing = True
score = 0
games_played = 0

item = ["Rock", "Paper", "Scisscors"]

while is_playing:

    games_played += 1
    user_choice = int(input("Type '0' for Rock, '1' for Paper, and '2' for scissors..."))
    computer_choice = random.randint(0, 2)

    if user_choice < 0 or user_choice > 2:
        print("You typed an invalid number, you lose!")
    else:
        print(f"You chose: {item[user_choice]} | Computer chose: {item[computer_choice]}")
        if user_choice == computer_choice:
            print("Draw!")
        elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (
                user_choice == 2 and computer_choice == 0):
            print("Computer Wins!")
        else:
            score += 1
            print("You win!")

    print(f"Current scoreboard: #Games Played {games_played} | #Score {score}")

    choice = input("Press 'y' to continue playing, 'n' to quit...")
    if choice == "n":
        is_playing = False