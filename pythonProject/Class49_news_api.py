import requests
import json
from datetime import datetime

query = input("Enter your category for news ? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-06-19&sortBy=publishedAt&apiKey=28df1762137c4ee6b77f29d8cb745a25"

response = requests.get(url)
news = response.json()

# beautified_news = json.dumps(news, indent=4)
# print(beautified_news)

i = 1
for article in news["articles"]:
    print(f"{i}. \nTitle: {article["title"]}")
    print(f"Description: {article["description"]}")

    iso_date = article["publishedAt"]

    # strptime is used to convert a string representing a date and/or time into a datetime object.
    datetime_obj = datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%SZ")

    date = datetime_obj.strftime("%B %d, %Y %I:%M %p")

    print(f"Date: {date}")
    print("\n---------------------------------------------------------------\n")
    i += 1

'''
some formats for datetime

%B: Full month name (e.g., July)
%d: Day of the month (zero-padded, e.g., 18)
%m: Month
%Y: Year with century (e.g., 2024)
%I: Hour (12-hour clock, zero-padded, e.g., 06)
%H: Hour (24 hour clock)
%M: Minute (zero-padded, e.g., 31)
%S: Seconds
%p: AM or PM (e.g., AM)
'''