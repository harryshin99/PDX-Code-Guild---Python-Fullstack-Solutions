"""
Creator: Harry Shin
Date: 21 Dec 2020
"""

import random

computers_num = random.randint(1, 10)

current_guess = input("Guess the computer's number from 1 - 10: ")

last_guess = 0

tries = 0

while True:

    if current_guess == 'done':
        print("Goodbye!")
        break

    while tries == 0:
        current_guess = int(current_guess)
        if current_guess == computers_num:
            print(f"You guessed the correct number of {computers_num}. You guessed {tries} time(s).")
            break
        elif current_guess > computers_num:
            current_guess = input("You guessed too high. Please try again: ")
        else:
            current_guess = input("You guessed too low. Please try again: ")
        tries += 1

    last_guess = int(current_guess)
    current_guess = int(current_guess)
    if current_guess == computers_num:
        print(f"You guessed the correct number of {computers_num}. You guessed {tries} time(s).")
        break
    elif current_guess > computers_num:
        print("Your guess was too high.")
        if abs(last_guess - computers_num) > abs(current_guess - computers_num):
            current_guess = input("Your current guess was closer. Please try again: ")
        else:
            current_guess = input("Your previous guess was closer. Please try again: ")
    else:
        if abs(last_guess - computers_num) < abs(current_guess - computers_num):
            current_guess = input("Your current guess was closer. Please try again: ")
        else:
            current_guess = input("Your previous guess was closer. Please try again: ")

    tries += 1