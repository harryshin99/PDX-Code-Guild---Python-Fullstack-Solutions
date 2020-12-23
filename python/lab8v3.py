"""
Creator: Harry Shin
Date: 21 Dec 2020
"""

import random

computers_num = random.randint(1, 10)

user_num = input("Guess the computer's number from 1 - 10: ")

tries = 0

while True:

    if user_num == 'done':
        print("Goodbye!")
        break

    tries += 1

    user_num = int(user_num)
    if user_num == computers_num:
        print(f"You guessed the correct number of {computers_num}. You guessed {tries} time(s).")
        break
    elif user_num > computers_num:
        user_num = input("You guessed too high. Please try again: ")
    else:
        user_num = input("You guessed too low. Please try again: ")