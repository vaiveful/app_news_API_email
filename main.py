import requests
from send_email_function import send_email

topic = "tesla"

api_key = "ca75c583631848aaaaf2f92210c4923f"
url = ("https://newsapi.org/v2/top-headlines?"
       "sources=techcrunch&"
       "apiKey=ca75c583631848aaaaf2f92210c4923f&"
       "language=en")

#Make request
request = requests.get(url)

#Get dictionary with data
content = request.json()

#Access the article titles and descriptions
body = ""
for article in content["articles"][:10]:
       if article["title"] is not None:
              body = ("Subject: Today's News" + "\n"
                      + body + article["title"] + "\n"
                      + article["description"] + "\n"
                      + article["url"] + 2*"\n")

body = body.encode("utf-8")
send_email(body)
