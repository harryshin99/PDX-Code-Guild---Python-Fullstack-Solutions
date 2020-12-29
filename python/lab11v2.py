"""
Creator: Harry Shin
Date: 23 Dec 2020
"""

print("Welcome to the Change Maker 5000 (tm)")

while True:

    nickels = 0.0
    dimes = 0.0
    nickels = 0.0
    pennies = 0.0
    output = []

    amount = float(input("Enter a dollar amount: "))

    quarters = amount // 0.25
    amount = round((amount - (quarters * 0.25)), 2)

    dimes = amount // 0.10
    amount = round((amount - (dimes * 0.10)), 2)

    nickels = amount // 0.05
    amount = round((amount - (nickels * 0.05)), 2)

    pennies = round((amount // 0.01), 2)

    if quarters == 1:
        output += [f"{int(quarters)} quarter"]
    elif quarters > 0:
        output += [f"{int(quarters)} quarters"]

    if dimes == 1:
        output += [f"{int(dimes)} dime"]
    elif dimes > 0:
        output += [f"{int(dimes)} dimes"]

    if nickels == 1:
        output += [f"{int(nickels)} nickel"]
    elif nickels > 0:
        output += [f"{int(nickels)} nickels"]
    
    if pennies == 1:
        output += [f"and {int(pennies)} penny"]
    elif pennies > 0:
        output += [f"{int(pennies)} pennies"]

    print(', '.join(output))

    answer = input("Would you like to make more change?  ").lower()
    if answer == "no":
        print("Have a good day!")
        break
