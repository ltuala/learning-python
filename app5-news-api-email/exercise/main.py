import requests
from send_email import send_email

api_key = "0d68c70f86fa43afad739206dd9d7850"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-10-20&sortBy=publishedAt&apiKey=0d68c70f86fa43afad739206dd9d7850"

request = requests.get(url)
content = request.json()
message = ""

for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None:
        article_message = article["title"] + "\n" + article["description"] + 2*"\n"
        message = message + article_message
    
message = message.encode("utf-8")
send_email(message)