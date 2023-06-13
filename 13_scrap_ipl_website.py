import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.iplt20.com/auction/2022"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")


div = soup.find_all("div", class_ = "ih-pcard-wrap")[1]

headers = div.find_all("th", class_= "skip-filter")
title = [t.text for t in headers]

table_body = div.find_all("tbody", {'id': 'pointsdata'})[0]

table_data = table_body.find_all('tr')

df = pd.DataFrame(columns=title)


for i in table_data:
    data = i.find_all('td')
    row = [tr.text for tr in data]
    l = len(df)
    df.loc[l] = row

print(df)
