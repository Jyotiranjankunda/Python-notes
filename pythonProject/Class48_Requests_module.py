# The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.

import requests
from bs4 import BeautifulSoup

url = "https://jsonplaceholder.typicode.com/posts"

# get request
get_response = requests.get(url)
print(get_response.text)

# post request
data = {
    "title": "Jyotiranjan",
    "body": "Software Engineer",
    "userId": "2698"
}

headers = {
    'Content-Type': 'application/json; charset=UTF-8'
}

post_response = requests.post(url, headers=headers, json=data)
print(post_response.text)

# bs4 Module
# There is another module called BeautifulSoup which is used for web scraping in Python

url = "https://www.geeksforgeeks.org/loops-in-java"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

# It will extract all the paragraph tags from the source code
for paragraph in soup.find_all("p"):
    print(paragraph.text)