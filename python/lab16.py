import requests
import string

space = string.whitespace

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

def use_requests():
    response = requests.get('https://www.gutenberg.org/files/64223/64223-0.txt')
    book = response.text
    return book

def num_of_char(book):
    for char in book:
        if char in space:
            book = book.replace(char, "")
    return len(book)

def num_of_words(book):
    return len(book.split())

def num_of_sentences(book):
    sentence_punct = ['.', '?', '!']
    sentence_count = 0
    for char in book:
        if char in sentence_punct:
            sentence_count += 1
    return sentence_count

def get_ari_score(char_num, word_num, sentence_num):
    result = round((4.71 * (char_num / word_num)) + (0.5 * (word_num / sentence_num)) - 21.43)
    if result > 14:
        result = 14
    return result

def get_book_name(book):
    book = book.split("\n")
    for word in book:
        if "Title" in word:
            book_name = word.replace("Title: ", "")
            book_name = book_name.replace("\r", "")
            # word = word[7:]
            return book_name

def main(): 

    book = use_requests()
    book_name = get_book_name(book)
    char_num = num_of_char(book)
    word_num = num_of_words(book)
    sentence_num = num_of_sentences(book)

    ari_score = get_ari_score(char_num, word_num, sentence_num)
    
    print(f"""
    ------------------------------------------------------------------------------------
    The ARI for {book_name} is {ari_score}.
    This corresponds to a {ari_scale[ari_score]['grade_level']} grade level of difficulty
    that is suitable for an average person {ari_scale[ari_score]['ages']} years old.
    ------------------------------------------------------------------------------------
    """)

main()