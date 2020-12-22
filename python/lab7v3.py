"""
Creator: Harry Shin
Date: 21 Dec 2020
"""

import random

print("Let's play Rock, Paper, Scissors, Lizard, Spock!")

moves = ['✊', '✋', '👉', '🖖', '🦎']

answer = "yes"

while answer == 'yes':

    user = input("Your moves are 'rock', 'paper', 'scissors', 'lizard', and 'spock'. Enter your move: ").lower()

    computer = random.choice(moves)

    if user == 'rock':
        user = '✊'
    elif user == 'paper':
        user = '✋'
    elif user == 'scissors':
        user = '👉'
    elif user == 'lizard':
        user = '🦎'
    else:
        user = '🖖'

    if user == computer:
        print(f"You entered {user}. The computer entered {computer}. It was a tie!")
    elif user == '✊':
        if computer == '🦎' or computer == '👉':
            print(f"You entered {user}. The computer entered {computer}. You win!")
        else:
            print(f"You entered {user}. The computer entered {computer}. You lose!")
    elif user == '👉':
        if computer == '✋ ' or computer == '🦎':
            print(f"You entered {user}. The computer entered {computer}. You win!")
        else:
            print(f"You entered {user}. The computer entered {computer}. You lose!")
    elif user == '✋':
        if computer == '✊' or computer == '🖖':
            print(f"You entered {user}. The computer entered {computer}. You win!")
        else:
            print(f"You entered {user}. The computer entered {computer}. You lose!")
    elif user == '🦎':
        if computer == '✋' or computer == '🖖':
            print(f"You entered {user}. The computer entered {computer}. You win!")
        else:
            print(f"You entered {user}. The computer entered {computer}. You lose!")
    elif user == '🖖':
        if computer == '✊' or computer == '👉':
            print(f"You entered {user}. The computer entered {computer}. You win!")
        else:
            print(f"You entered {user}. The computer entered {computer}. You lose!")

    answer = input("Enter 'yes' if you want to play again: ").lower()

