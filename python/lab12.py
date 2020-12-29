
print("Welcome to Black Jack advisor. Your available cards are: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K")

first_card = input("What is your first card: ").upper()
second_card = input("What is your second card: ").upper()
third_card = input("What is your third card: ").upper()

card_values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

for value in card_values:
    if first_card in value:
        first_card = card_values[value]
        first_card = int(first_card)
        break

for value in card_values:
    if second_card in value:
        second_card = card_values[value]
        second_card = int(second_card)
        break

for value in card_values:
    if third_card in value:
        third_card = card_values[value]
        third_card = int(third_card)
        break

total = first_card + second_card + third_card

if total < 17:
    print(f"{total}: Hit")
elif 17 <= total < 21:
    print(f"{total}: Stay")
elif total == 21:
    print(f"{total} Blackjack!")
else:
    print(f"{total}: Already Busted")