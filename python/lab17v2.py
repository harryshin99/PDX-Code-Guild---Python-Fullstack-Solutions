import requests
import json

def get_data(url):

    headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}

    data = requests.get(url, headers=headers)

    data = json.loads(data.text)
    return data

while True:
    keyword = input("Enter a keyword to search for quotes: ")
    page = 1

    while True:
        print(f"25 quotes associated with {keyword} - page {page}")

        url = 'https://favqs.com/api/quotes?page=' + str(page) + '&filter=' + keyword

        quotes = dict()

        data = get_data(url)

        for index, value in enumerate(data['quotes']):
            quotes[index] = value

        for key, val in quotes.items():
            if isinstance(val, dict):
                print(val.get('body'))

        next_page = input("enter 'next page' or 'done': ")
        if next_page == 'done':
            break
        elif next_page == 'next page':
            page += 1