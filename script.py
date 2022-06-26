from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys 
import pandas as pd
import re 

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://store.steampowered.com/search/?sort_by=Price_ASC&maxprice=70&category1=998%2C996&category2=29&os=win")
driver.maximize_window()
ScrollNumber = 2
for i in range(1, ScrollNumber):
    driver.execute_script("window.scrollTo(1,1000)")
    time.sleep(3)
page = BeautifulSoup(driver.page_source, 'html.parser')
links = page.findAll('a', class_='search_result_row ds_collapse_flag app_impression_tracked')
pages = page.findAll('a')
games = []
for page in pages:
    if page.get('href') is not None:
        if 'store.steampowered.com/app/' in page.get('href'):
            appid = page.get('data-ds-appid')
            prices = page.find('div', class_='col search_price_discount_combined responsive_secondrow')
            title = page.find('span', class_='title')
            div = page.find('div' , class_='col search_price discounted responsive_secondrow')
            price = prices.get('data-price-final')
            discount = page.find('div', class_="col search_discount responsive_secondrow")
            discount = (discount.text)
            discount = re.sub('[^0-9]', '', discount)
            div = (div.text).split()
            if "," in appid:
                games.append((title.text, appid + "es un pack", div[2],discount))
            else:
                games.append((title.text, appid, div[2],discount))
            
print(len(games))
print(games)

df = pd.DataFrame(games, columns=['Title', 'AppID', 'Price', 'Discount'])
print(df)    
df.to_json('games.json', orient='records', indent=4)




#href="https://store.steampowered.com/search/?sort_by=Price_ASC&sort_order=ASC&category1=998%2C996&category2=29&price=%2C70&os=win&maxprice=70&page=2"

