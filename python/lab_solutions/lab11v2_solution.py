

# coins = [
#     ('half-dollar', 50),
#     ('quarter', 25),
#     ('dime', 10),
#     ('nickel', 5),
#     ('penny', 1)
# ]

# num_coins = []

# pennies = input("Enter dollar amount: $")
# pennies = float(pennies)

# pennies *= 100
# pennies = int(pennies)

# for coin in coins:
#     quantity = (coin[0], pennies // coin[1])
#     pennies -= coin[1] * quantity[1]
#     num_coins.append(quantity)

# for coin in num_coins:
#     print(f"{coin[0]}: {coin[1]}")


#-------------------------------------------------# Version with dictionaries


coins = {
    "half-dollar": 50,
    "quarters": 25,
    "dimes": 10,
    "nickels": 5,
    "pennies": 1
}

num_coins = {}

pennies = input("Enter dollar amount: $")
pennies = float(pennies)

pennies *= 100
pennies = int(pennies)

for name in coins:
    value = coins[name]
    quantity = pennies // value
    num_coins[name] = quantity
    pennies -= quantity * value

for name in num_coins:
    print(f"{name}: {num_coins[name]}")