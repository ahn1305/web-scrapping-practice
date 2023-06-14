import requests
from bs4 import BeautifulSoup
import pandas as pd
Names = []
Prices = []
Desc = []

for i in range(1,4):
    url = f"https://www.flipkart.com/search?q=mobile+phones+under+5000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"

    r =requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")

    names = box.find_all("div", class_ = "_4rR01T")
    for i in names:
        Names.append(i.text)

    prices = box.find_all("div", class_ = "_30jeq3 _1_WHN1")
    for j in prices:
        Prices.append(j.text)

    descs = box.find_all("ul",class_ = "_1xgFaf")
    for k in descs:
        Desc.append(k.text)


df = pd.DataFrame({"Name": Names, "Price": Prices, "Description": Desc})
# print(df)

print(len(Names), len(Prices), len(Desc))

df.to_csv("mobiles.csv")