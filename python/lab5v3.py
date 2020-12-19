"""
Creator: Harry Shin
Date: 17 Dec 2020
"""

import random

eye_list = ["^", "-", "o", "+", "=", ".", "T", "TT", "Q", "*", ">"]

mouth_list = ["__", " . ", ",", "c", "_"]

side_list = ["(", "[", "{", ""]

num = 0
while num < 5:

    random_eye = random.choice(eye_list)
    if random_eye == ">":
        right_eye = "<"
    else:
        right_eye = random_eye

    random_side = random.choice(side_list)
    if random_side == "(":
        right_side = ")"
    elif random_side == "[":
        right_side = "]"
    elif random_side == "{":
        right_side = "}"
    elif random_side == "":
        right_side = ""

    print(random_side + random_eye + random.choice(mouth_list) + right_eye + right_side)
    num += 1