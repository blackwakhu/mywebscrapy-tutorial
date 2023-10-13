import requests
from bs4 import BeautifulSoup

"""
use requests to download the url 
the syntax is 
  response = request.get(url)
now we are going to use a simple url 'https://scrapeme.shop/live/'
"""

response = requests.get("https://scrapeme.shop/live/")

"""
we are going to use beautiful soup to get the html content from requests.content
"""

soup = BeautifulSoup(response.content, "html.parser")

"""create a selector for a css attribute"""
link_elems = soup.select("a[href]")

"""get the urls"""
urls = []

for link_elem in link_elems:
  url = link_elem["href"]
  if "https://scrapeme.live/" in url:
    urls.append(url)
