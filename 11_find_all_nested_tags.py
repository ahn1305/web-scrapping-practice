import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

boxes = soup.find_all("div", class_ = "col-sm-4 col-lg-4 col-md-4")

#print(len(boxes))

# for individual items
box = soup.find_all("div", {'class': 'col-sm-4 col-lg-4 col-md-4'})[2]

title = box.find("a").text
print(title[:-3])

desc = box.find("p", {'class':'description'}).text
print(desc)


new_data = soup.find_all("ul", class_ = "nav")[2]

print(new_data.find("li").text)