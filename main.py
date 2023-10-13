import requests
from bs4 import BeautifulSoup

"""
use requests to download the url 
the syntax is 
  response = request.get(url)
now we are going to use a simple url 'https://scrapme.shop/live/'
"""

response = requests.get("https://scrapme.shop/live/")
