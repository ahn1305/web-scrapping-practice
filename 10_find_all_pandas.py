import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

# fetching the required data
names = soup.find_all("a", class_ = "title")
prices = soup.find_all("h4", class_ = "pull-right price")
desc = soup.find_all("p", class_ = "description")
reviews = soup.find_all("p", {'class':'pull-right'})

#converting the data into lists
product_list = [p.text for p in names]
price_list = [pr.text for pr in prices]
desc_list = [d.text for d in desc]
reviews_list = [re.text for re in reviews]


df = pd.DataFrame({
    "ProductName": product_list,
    "Price": price_list,
    "Description": desc_list,
    "Reviews": reviews_list
})

df.to_csv("ProductList.csv")

# to convert to excel
'''
pip install openpyxl
then replace .to_csv to .to_excel
'''