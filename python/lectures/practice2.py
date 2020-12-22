# def double_letters(word):
    # i = 0
    # output = ''
    # while i < len(word):
    #     output += word[i]* 2
    #     i += 1
    # return output

#     output = ''
#     for c in word:
#         output += c * 2
#     return output

# print(double_letters('hello'))


# def count_letter(letter, word):
#     num_string = 0
#     for char in word:
#         if letter == char:
#             num_string += 1
#     return num_string

    # return word.count(letter) #string method count

# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2

def latest_letter(word):
    # letter = ''
    # for char in word:
    #     if char > letter:
    #         letter = char
    # return letter

    word = list(word)
    word.sort()
    return word [-1]

print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v


# def count_hi(text):
#     return text.count("hi")



# print(count_hi('hihi')) # 2
# print(count_hi('hihihellohihi')) # 2

# import string
# def snake_case(text):
#     text = text.lower()
#     text = text.replace(" ", "_")
#     for char in text:
#         if char in string.punctuation and char != '_':
#             text = text.replace(char, '')
#     return text

# print(snake_case('Hello World!')) # hello_world
# print(snake_case('This is another example.')) # this_is_another_example