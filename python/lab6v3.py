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

num_lowercase = input("Enter your number of lowercase, uppercase, numbers, and special characters separated by commas: ")

split_num = num_lowercase.split(", ")

password = ""

for i in range(int(split_num[0])):
    password += random.choice(lowercase)

for i in range(int(split_num[1])):
    password += random.choice(uppercase)

for i in range(int(split_num[2])):
    password += random.choice(digits)
    
for i in range(int(split_num[3])):
    password += random.choice(punctuation)

password = list(password)
random.shuffle(password)
password = ''.join(password)

print(f"Your password is {password}")