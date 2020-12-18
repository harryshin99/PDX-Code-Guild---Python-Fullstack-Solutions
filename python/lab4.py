"""
Creator: Harry Shin
Date: 17 Dec 2020
"""

import random

predictions = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely!",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

print("Hello, welcome to the magic 8 ball!")

question = input("Ask me anything: ")

print(random.choice(predictions))

while question != "done":
    question = input("Enter 'done' if you'd like to quit. Otherwise, ask me another question: ")
    if question == 'done':
        print("Goodbye!")
        break
    print(random.choice(predictions))