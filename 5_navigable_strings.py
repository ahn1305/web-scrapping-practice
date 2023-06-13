# text inside the tags are called navigable tags
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"
r = requests.get(url)


soup = BeautifulSoup(r.text, "lxml")

tag = soup.div.p    
print(tag.string) # fetch string from the tag using .string method

print(soup.div.a.button.span.string)