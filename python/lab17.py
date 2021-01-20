
import requests
import json

url = "https://favqs.com/api/qotd"

response = requests.get(url)

data = json.loads(response.text)

# print(data)

print(data['quote']['author'])
print(data['quote']['body'])   