import requests
from bs4 import BeautifulSoup

url = "https://ahnashwin1305.medium.com/"

r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")

articles = soup.find_all("article")

for index,i in enumerate(articles):
    if i.img != None:
        print(index,i.img['src'])
    elif i.img == None:
        print(index,i.img)
    else:
        pass