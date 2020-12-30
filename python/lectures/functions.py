# def pretty_print():
#     print("hello world")

# pretty_print()


import random

def num_matches(winning, current):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == current[i]:
            matches += 1
    return matches

def generate_ticket():
    ticket = []
    for i in range(6):
        num = random.randint(1, 99)
        while num in ticket:
            num = random.randint(1, 99)
        ticket.append(num)
    return ticket

    # return[random.randint(1, 99) for i in range(6)]

winning_ticket = generate_ticket()
power_ball = random.randint(0, 99)

balance = 0
expenses = 0
earnings = 0
occurrences = {}

for x in range(100000):
    current_ticket = generate_ticket()
    current_powerball = random.randint(0, 99)

    balance -= 2
    expenses += 2

    matches = num_matches(winning_ticket, current_ticket)

    if matches not in occurrences:
        occurrences[matches] = 1
    else:
        occurrences[matches] += 1

    winnings = {
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    }

    if current_powerball == power_ball:
        balance += winnings[matches] * 2
        earnings += winnings[matches] * 2
    else:
        balance += winnings[matches]
        earnings += winnings[matches]

for t in occurrences:
    print(f"{t} matched {occurrences[t]} times.")

print(f"${balance}")

print(f"ROI: {((earnings - expenses)/expenses)*100}%")