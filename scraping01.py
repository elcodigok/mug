import requests
from bs4 import BeautifulSoup

req = requests.get("https://danielmaldonado.com.ar")
soup = BeautifulSoup(req.content, 'html.parser')

print(soup.find_all("h1")[0].get_text())
