import random

card_number = "123456789123456"

card_list = list(card_number)

for num in range(len(card_list)):
    # num = int(num)
    card_list[num] = int(card_list[num])

print(card_list)