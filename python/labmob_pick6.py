import random

# Generate a list of 6 random numbers representing the winning tickets
winning_ticket = []

while len(winning_ticket) < 6:
    winning_ticket.append(random.randint(1, 99))

# Start your balance at 0
balance = 0

# Loop 100,000 times, for each loop:
counter = 0
while counter < 100000:
    counter += 1
    user_ticket = []
# Generate a list of 6 random numbers representing the ticket
    while len(user_ticket) < 6:
        user_ticket.append(random.randint(1, 99))
    
# Subtract 2 from your balance (you bought a ticket)
    balance -= 2

# Find how many numbers match
    round_matches = 0
    for idx in range(len(winning_ticket)):
        if winning_ticket[idx] == user_ticket[idx]:
            round_matches += 1
            print(round_matches)
            
# Add to your balance the winnings from your matches
    if round_matches == 1:
        balance += 4
    elif round_matches == 2:
        balance += 7
    elif round_matches == 3:
        balance += 100
    elif round_matches == 4:
        balance += 50000
    elif round_matches == 5:
        balance += 1000000
    elif round_matches == 6:
        balance += 25000000

# After the loop, print the final balance
print(balance)
