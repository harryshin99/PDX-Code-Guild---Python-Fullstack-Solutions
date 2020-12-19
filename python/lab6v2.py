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

all_char = lowercase + uppercase + digits + punctuation

length = input("How long do you want your number to be? Please enter a whole number: ")

length = int(length)

password = ""

for num in range(length):
    password += random.choice(all_char)

print(f"Your password is {password}")