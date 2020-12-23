import string

lowercase = string.printable

user_choice = int(input("Enter your desired value for encryption rotation: "))

encrypted_lowercase = lowercase[user_choice:] + lowercase[:user_choice]

user_string = input("Enter the word you would like to encrypt: ")

user_string_list = list(user_string)
lowercase_list = list(lowercase)

secret_string = []
for char in user_string_list:
    if char in lowercase_list:
        index = lowercase_list.index(char)
        secret_string.append(encrypted_lowercase[index])

secret_string = ''.join(secret_string)
print(f"Your encrypted word '{user_string}' at a rotation of {user_choice} is '{secret_string}'.")