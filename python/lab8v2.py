"""
Creator: Harry Shin
Date: 21 Dec 2020
"""

import random

computers_num = random.randint(1, 10)

user_num = input("Enter 'done' at anytime to quit. Guess the computer's number from 1 - 10: ").lower()

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
    else:
        user_num = input("That is not correct. Please try again: ")