"""
Creator: Harry Shin
Date: 17 Dec 2020
"""

import random

eye_list = [":", ";", "=", "X", "8"]

nose_list = ["-", "^", "o", "c", ""]

mouth_list = ["(", ")", "]", ">", "D", "3", "}", "X", "O", "P"]

num = 0

while num < 5:
    print(random.choice(eye_list) + random.choice(nose_list) + random.choice(mouth_list))
    num += 1