import requests, re
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

# get all data related to a specific word using re

data = soup.find_all(string = re.compile("Asus"))
print(len(data))