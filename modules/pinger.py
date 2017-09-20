import requests
from bs4 import BeautifulSoup


# iPhone X 64gb model purchase page
URL = "https://www.apple.com/us-hed/shop/buy-iphone/iphone-x/5.8-inch-display-64gb-silver-tmobile"

# Query the URL and store the HTML content
page = requests.get(URL).text

print(page)
