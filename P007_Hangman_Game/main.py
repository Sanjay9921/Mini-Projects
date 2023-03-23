#Import Libraries
from hangman_art import *
import random
from hangman_words import *

#Randomly choose a word from the list and then display
word = random.choice(word_list).lower()
n_word = len(word)

#global variable
lives=6
end_of_game = False

#Code
#Display Logo
print(logo)

#Test
print(f"Psst, the solution is {word}")

#Display current guess
guess_word = ["_" for i in range(n_word)]

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Case1
    #Already guessed
    if guess in guess_word:
        print(f"You've already guessed {guess}")

    #Case2
    #New word guessed
    for i in range(n_word):
        letter = word[i]
        if letter==guess:
            guess_word[i] = letter

    if "_" not in guess_word:
        end_of_game = True
        print("You won!")

    #Case3
    #Wrong letter guessed
    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        lives-=1

        if lives==0:
            end_of_game = True
            print(f"You lose! The word was: {word}")

    #Display current guess
    print(f"{' '.join(guess_word)}")

    #Display the Hangman Stage
    print(stages[lives])



