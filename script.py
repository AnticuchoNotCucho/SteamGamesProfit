from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://store.steampowered.com/search/?sort_by=Price_ASC&maxprice=70&category1=998%2C996&category2=29&os=win")

page = BeautifulSoup(driver.page_source, 'html.parser')
list = page.find('div', id='search_resultsRows')
links = page.findAll('a', class_='search_result_row ds_collapse_flag')
for link in links:
    appid = link.get('data-ds-appid')
    prices = link.find('div', class_='col search_price_discount_combined responsive_secondrow')
    title = link.find('span', class_='title')
    price = prices.get('data-price-final')
    if "," in appid:
        print(title.text, appid, "es un pack", price)
    else:
        print(title.text, appid, price)
    



#for title in titles:
    #print(title.text)