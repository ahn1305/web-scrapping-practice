import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

laptops = soup.find_all("a", class_='title')
prices = soup.find_all("h4", class_ = 'pull-right price')

# for index, (l, p) in enumerate(zip(laptops, prices), start=1):
#     print(index, l.text, p.text)


for index, value in enumerate(laptops):
    print(index,'\t',value.string)