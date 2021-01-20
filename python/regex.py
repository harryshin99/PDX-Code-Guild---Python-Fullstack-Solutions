

# \d # all digits
# \D # all non-digits

# \w # all char
# \W # all non-char

# \s # all whitespace
# \S # all non-whitespace


# \w\w\w\ # 3 char next to each other

# \d\d\d # 3 digits next to each other

# \d{3}-\d{3}-\d{4} # phone number

# \w{7}@\w[5]\.\w{3}


# [\w\.]+@\w+\.\w+


# ^this \w+

# [w+ owl$ # dollar ends with that dollar sign.


# import re

# with open('text_to_search.txt', 'r') as file:
#     text = file.read

# people = re.findall(r'Mrs\.* \w+|Mr\.* \w+|Ms\.* \w+', text)

# print(people)
# print(r'\t hello \n class owl')


# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)
# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String
# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)


import re
import json

with open('data.txt', 'r') as file:
    text = file.read()

names = re.findall(r'^[a-zA-Z]{3,} [a-zA-Z\-]{3,}', text, flags = re.MULTILINE)
phone_numbers = re.findall(r'\d+-\d+-\d+', text)
addresses = re.findall(r'\d+ .+', text, flags=re.MULTILINE)
emails = re.findall(r'\w+@\w+\.\w+', text)

# print(names)
# print(phone_numbers)
# for address in addresses:
#     print(address)
# print(emails)
# print(f'names: {len(names)} phone#: {len(phone_numbers)}, addresses: {len(addresses)}, emails: {len(emails)}')

contacts = []

for index in range(len(names)):
    firstlast = names[index].split()
    contact = {
        'first_name': firstlast[0],
        'last_name': firstlast[1],
        'phone': phone_numbers[index],
        'address': addresses[index],
        'email': emails[index]
    }
    contacts.append(contact)

# for contact in contacts:
#     print(contact)

with open('contacts.json', 'w') as file:
    text = json.dumps(contacts)
    file.write(text)