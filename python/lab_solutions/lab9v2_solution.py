import string

all_char = string.printable

user_string = input("Enter your message to encrypt: ")
rotation = int(input("Enter the amount to be rotated: "))

output =""
for char in user_string:
    if char in all_char:
        index = all_char.find(char)
        index += rotation
        output += all_char[index % len(all_char)]
    else:
        output += char

print(f"{user_string} is encrypted to {output}.")