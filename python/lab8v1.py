"""
Creator: Harry Shin
Date: 21 Dec 2020
"""

import random

computers_num = random.randint(1, 10)

user_num = int(input("Guess the computer's number from 1 - 10: "))

attempts = 0
while attempts < 10:

    attempts += 1

    if user_num == computers_num:
        print(f"You guessed the correct number of {computers_num}. You guessed {attempts} time(s).")
        break
    else:
        user_num = int(input("That is not correct. Please try again: "))

print(f"You did not guess the correct number after {attempts} times. The correct number was {computers_num}.")