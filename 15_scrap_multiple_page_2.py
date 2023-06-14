import requests, pandas as pd, re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_binary, time


# Options keep the Chrome window open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Adding options to Chrome and creating the browser variable
browser = webdriver.Chrome(options=chrome_options)

browser.get("https://www.airbnb.co.in/s/Chennai--India/homes?adults=1&place_id=ChIJYTN9T-plUjoRM9RjaAunYW4&refinement_paths%5B%5D=%2Fhomes&tab_id=home_tab&query=Chennai%2C%20India&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-07-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&ne_lat=13.469483920131612&ne_lng=81.08925349361385&sw_lat=12.299470513397951&sw_lng=79.78222376949276&zoom=9&zoom_level=9&search_by_map=true&search_type=user_map_move")
time.sleep(15)
Location = []
Desc = []
TotalBeds = []
Prices = []

url = browser.current_url

for an in range(1,3):
    r = requests.get(url)

    soup = BeautifulSoup(r.text, "lxml")

    
    time.sleep(5)
    box = soup.find("div", class_ = "f1ym1fv dir dir-ltr")
    hotels = box.find_all("div", class_ = "t1jojoys dir dir-ltr")
    for i in hotels:
        Location.append(i.text)

    descs = box.find_all("span", class_ = "t6mzqp7 dir dir-ltr")
    for j in descs:
        Desc.append(j.text)

    b = box.find_all("div", class_ = "g1qv1ctd c1v0rf5q dir dir-ltr")
    for k in b:
        val = k.find("span", class_ = "dir dir-ltr").text
        if "bed" not in val:
            val = k.find("span", class_ = "t6mzqp7 dir dir-ltr").text
        
        TotalBeds.append(val)

    prices = box.find_all("div", class_ = "_1jo4hgw")
    for p in prices:
        Prices.append(p.text)

    time.sleep(5)
    nxt_page = browser.find_element("xpath", '//*[@id="site-content"]/div/div[3]/div/div/div/nav/div/a[5]').click()
        
    print(f"{an} page done")
df = pd.DataFrame({"Location": Location, "Description": Desc, "TotalBeds":TotalBeds, "Prices": Prices})
print(df)