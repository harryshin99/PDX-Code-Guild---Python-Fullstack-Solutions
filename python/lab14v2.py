
digits = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "one-hundred",
    200: "two-hundred",
    300: "three-hundred",
    400: "four-hundred",
    500: "five-hundred",
    600: "six-hundred",
    700: "seven-hundred",
    800: "eight-hundred",
    900: "nine-hundred"
}

rem_digits = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
    1: "one hundred"
}

def validate_input(message):
    while True:
        number = input(message)
        try:
            number = int(number)
            if 0 <= number <= 999:
                return number
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid whole number between 0 - 999: ")

def convert_number(number):
    while True:
        if number in digits:
            return digits[number]
        elif number <= 99:
            return rem_digits[number//10] + '-' + digits[number % 10]
        else:
            hundreds = digits[number // 100]
            hundred_num = {key for key, value in digits.items() if value == hundreds}
            hundred_num = list(hundred_num)
            hundred_num = int(hundred_num[0])
            number = number - (hundred_num * 100)
            if number in digits:
                return hundreds + "-hundred-" + digits[number]
            else:
                return hundreds + "-hundred-" + rem_digits[number//10] + '-' + digits[number % 10]

def main():

    number = validate_input("Enter the number you want to stringify: ")
    converted_number = convert_number(number)

    print(f"{number} is {converted_number}.")

main()