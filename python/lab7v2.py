"""
Creator: Harry Shin
Date: 21 Dec 2020
"""

import random

print("Let's play Rock, Paper, Scissors!")

moves = ['✊', '✋', '👉']

answer = "yes"

while answer == 'yes':

    user = input("Your moves are 'rock', 'paper', and 'scissors'. Enter your move: ").lower()

    computer = random.choice(moves)

    if user == 'rock':
        user = '✊'
    elif user == 'paper':
        user = '✋'
    else:
        user = '👉'

    if user == computer:
        print(f"You entered {user}. The computer entered {computer}. It was a tie!")
    elif user == '✊':
        if computer == '✋':
            print(f"You entered {user}. The computer entered {computer}. You lose!")
        else:
            print(f"You entered {user}. The computer entered {computer}. You win!")
    elif user == '👉':
        if computer == '✋':
            print(f"You entered {user}. The computer entered {computer}. You win!")
        else:
            print(f"You entered {user}. The computer entered {computer}. You lose!")
    elif user == '✋':
        if computer == '✊':
            print(f"You entered {user}. The computer entered {computer}. You win!")
        else:
            print(f"You entered {user}. The computer entered {computer}. You lose!")

    answer = input("Enter 'yes' if you want to play again: ").lower()

