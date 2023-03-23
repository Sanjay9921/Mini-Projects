#Libraries
from icon import *
import os

#Functions
def welcome_msg():
    #print(icon)
    #display(Image(filename="images/roger.jpg"))
    print("\n")
    print("Welcome to Treasure Island!")
    print("Your mission is to find the Treasure (Obviously, I mean that is the game. Clarity much?)")
    print("You are Patrick Bateman, begin your search !")


def cross_road():
    while True:
        choice = input("You reach a crossroad. Enter 'left' or 'right'...").casefold()
        if choice not in ["left", "right"]:
            print("Try Again! Please enter only 'left' or 'right'!")
        else:
            break

    return choice


def lake():
    while True:
        choice = input(
            "You reach a lake with an island in the middle. Type 'wait' to wait for a boat or 'swim' to swim across.").casefold()
        if choice not in ["wait", "swim"]:
            print("Try Again! Please enter only 'wait' or 'swim'!")
        else:
            break

    return choice


def colored_doors():
    while True:
        choice = input(
            "You reach the island and see a house with three colored doors to choose from - 'red', 'blue', 'yellow'.").casefold()
        if choice not in ["red", "blue", "yellow"]:
            print("Try Again! Please enter only 'red' or 'blue' or 'yellow'!")
        else:
            break

    return choice


def treasure_island():
    welcome_msg()

    direction = cross_road()
    if direction == "left":
        choice = lake()
        if choice == "wait":
            door = colored_doors()
            if door == "yellow":
                #display(Image(filename="images/whitebeard.jpg"))
                print("You found the legendary One Piece !")
            elif door == "red":
                #display(Image(filename="images/ace.jpg"))
                print("You are burned in a fire! Game Over!")
            else:
                #display(Image(filename="images/titans.jpeg"))
                print("You are eaten (alive) by monsters. Game Over!")
        else:
            #display(Image(filename="images/kisame.jpg"))
            print("You are attacked by a trout! Game Over!")
    else:
        #display(Image(filename="images/shikamaru.jpg"))
        print("You fall into a hole! Game Over!")

treasure_island()

