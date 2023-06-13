import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ticker.finology.in/"
r = requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_ = "table table-sm table-hover screenertable")

headers = table.find_all("th")
rows = table.find_all("tr")

titles = [t.text for t in headers]


df = pd.DataFrame(columns=titles)

for i in rows[1:]:
    data = i.find_all('td')
    row = [tr.text for tr in data]
    l = len(df)
    df.loc[l] = row

print(df)