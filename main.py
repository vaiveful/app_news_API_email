import requests
from send_email_function import send_email

api_key = "XXXX"
url = ("https://newsapi.org/v2/top-headlines?"
       "sources=techcrunch&apiKey=ca75c583631848"
       "aaaaf2f92210c4923f")

#Make request
request = requests.get(url)

#Get dictionary with data
content = request.json()

#Access the article titles and descriptions
body = ""
for article in content["articles"]:
       if article["title"] is not None:
              body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)
