#Libraries
import random

#Internal Files
from symbols import *
from numbers import *
from letters import *

#Functions
def random_password_generator(n:int, char_list)->str:
    password = ""
    n_char_list = len(char_list)
    for i in range(n):
        random_index = random.randint(0,n_char_list-1)
        random_char = char_list[random_index]
        password += str(random_char)
    return password

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password ?"))
n_number = int(input("How many numbers would you like in your password ?"))
n_symbols = int(input("How many symbols would you like in your password ?"))

password_letters = random_password_generator(n_letters, letters)
password_numbers = random_password_generator(n_letters, numbers)
password_symbols = random_password_generator(n_letters, symbols)

password = password_letters + password_symbols + password_numbers

#Before Shuffling
print(password)

#Shuffle the password
shuffled_password = list(password)
random.shuffle(shuffled_password)

#After Shuffling
password = "".join(char for char in shuffled_password)
print(password)

