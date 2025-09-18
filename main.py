import requests

api_key = "ca75c583631848aaaaf2f92210c4923f"
url = ("https://newsapi.org/v2/top-headlines?"\
       "sources=techcrunch&apiKey=ca75c583631848"\
       "aaaaf2f92210c4923f")

#Make request
request = requests.get(url)

#Get dictionary with data
content = request.json()

#Access the article titles and descriptions
for article in content["articles"]:
       print(article["title"])
       print(article["description"])
