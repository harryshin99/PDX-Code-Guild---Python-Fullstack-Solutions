import requests
import json


headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}




for quote in quotes:
    print(quote['body'])
    print(f"\t--{quote['author']}")

while not(data['last_page']):
    next = input("Do you want to see the next page of results? ").lower()
    if next in ['yes', 'y', 'yeah', 'next']:
        page += 1
        url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
        response = requests.get(url, headers = headers)
        data = json.loads(response.text)
        quotes = data['quotes']
        for quote in quotes:
            print(quote['body'])
            print(f"\t--{quote['author']}")
    else:
        break