import requests

api_key = "0d68c70f86fa43afad739206dd9d7850"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-10-20&sortBy=publishedAt&apiKey=0d68c70f86fa43afad739206dd9d7850"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
