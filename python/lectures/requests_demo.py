import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/users/")

data = json.loads(response.text)

# for user in data:
#     print(user['name'])
#     print(user['email'])
#     print(user['phone'])
#     print('-'*12)


response = requests.get("https://jsonplaceholder.typicode.com/posts/")

data = json.loads(response.text)

for user in data:
    print(user['userId'])
    print(user['id'])
    print(user['title'])
    print(user['body'])
    print('-'*12)