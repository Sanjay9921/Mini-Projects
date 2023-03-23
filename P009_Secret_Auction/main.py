#Libraries
from art import *

#Functions
def find_highest_bidder(record):
    highest_bid = 0
    winner = ""

    for bidder, bid in record.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = bidder

    print(f"The winner is {winner} with a bid of {highest_bid}!")

#Global Variables
end_auction = False
record = {}

print(logo)
while not end_auction:
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    record[name] = bid

    choice = input("Any other bidders ? Type 'Y' or 'N'").casefold()
    if choice=="n":
        end_auction = True
        find_highest_bidder(record)

