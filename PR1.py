import requests
from bs4 import BeautifulSoup

URL = 'https://www.coingecko.com'
page = requests.get(URL)
print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="challenge-running")
print(results.prettify())
