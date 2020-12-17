"""
Creator: Harry Shin
Date: 16 Dec 2020
"""

score = input("Please enter your grade between 0 - 100: ")

score = int(score)

if 90 <= score <= 100:
    letter_grade = "A"
elif 80 <= score <= 89:
    letter_grade = "B"
elif 70 <= score <= 79:
    letter_grade = "C"
elif 60 <= score <= 69:
    letter_grade = "D"
elif 0 <= score <= 59:
    letter_grade = "F"
else:
    letter_grade = "N/A"
    print(f"The {score} you entered was out of range.")

mod_score = score % 10

if 100 >= score > 59:
    if score == 100:
        letter_grade += '+'
    elif 9 >= mod_score >= 6:
        letter_grade += '+'
    elif 3 >= mod_score >= 0:
        letter_grade += '-'

print(f"Your grade is {letter_grade}.")