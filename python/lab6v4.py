"""
Creator: Harry Shin
Date: 18 Dec 2020
"""

import random
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

all_char = [lowercase, uppercase, digits, punctuation]

num_lowercase = input("Enter your number of lowercase, uppercase, numbers, and special characters separated by commas: ")

split_num = num_lowercase.split(", ")

password = ""

i = 0

for x in split_num:
    for num in range(int(split_num[i])):
        password += random.choice(all_char[i])
    i += 1

password = list(password)
random.shuffle(password)
password = ''.join(password)

print(f"Your password is {password}")