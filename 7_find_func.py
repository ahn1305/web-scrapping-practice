import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

# for i,c in enumerate(soup.find_all('a', 'title')):
#     print(i,c.string)

#normal way to do this
print(soup.find('h4', {'class':'pull-right price'}))
print(soup.find('p' , {'class':'pull-right'}))

# alternative way to do this
print(soup.find("p", class_ = "pull-right"))


# using find only fetches the very first value, so we have to use an alternative which is find_all