import requests
from bs4 import BeautifulSoup

url = "https://example.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

par = soup.find('h1')
print(par)