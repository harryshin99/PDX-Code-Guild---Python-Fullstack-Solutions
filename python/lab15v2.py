import requests
import string

punct = string.punctuation
digits = string.digits

def use_requests():
    response = requests.get('https://www.gutenberg.org/files/64217/64217-0.txt')
    book = response.text
    return book

def remove_punct(book):
    for char in book:
        if char in punct:
            book = book.replace(char, " ")
    return book

def word_dict(book):
    word_dict = {}
    item = 0
    while item < len(book) - 1:
        pair = book[item] + " " + book[item + 1]
        if pair in word_dict:
            word_dict[pair] = word_dict[pair] + 1
        else:
            word_dict[pair] = 1
        item += 1
    return word_dict

def word_count_output(word_count):
    for key, value in word_count.items():
        print(key, ' : ', value)

def word_count_top_ten(word_count):
    words = list(word_count.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
    
def main(): 

    book = use_requests().lower()

    book = remove_punct(book).split()

    word_count = word_dict(book)

    word_count_output(word_count)

    word_count_top_ten(word_count)

main()