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
appid = '1334590'
url = "https://www.steamcardexchange.net/index.php?gamepage-appid-"+appid
driver.get(url)
page = BeautifulSoup(driver.page_source, 'html.parser')
first_row = page.find('div', class_='showcase-element-container card')
second_row = first_row.find_next ('div', class_='showcase-element-container card')
third_row = second_row.find_next ('div', class_='showcase-element-container card')
fourth_row = third_row.find_next ('div', class_='showcase-element-container card')
amount_cards = first_row.find('span', class_='element-count')
amount_cards = amount_cards.text
amount_cards = amount_cards.split()
amount_cards = int(amount_cards[3])
print(amount_cards)
if amount_cards > 5:
    for cards in first_row:
        title = cards.find('span', class_='element-text')
        price = cards.find('a', class_='button-blue')
        if not title:
            print('No Card')
        else:
            print(title.text)
            print(price.text)
            
    for cards in second_row:
        title = cards.find('span', class_='element-text')
        if not title:
            print('No Card')
        else:
            print(title.text)
            print(price.text)
# if amount_cards <= 5 :
#     for cards in first_row:
#         title = cards.find('span', class_='element-text')
#     if not title:
#         print('No Card')
#     else:
#         print(title.text,' ')
#         print(cards.text)
# elif amount_cards > 5:
#     for cards in first_row:
#         title = cards.find('span', class_='element-text')
#     if not title:
#         print('No Card')
#     else:
#         print(title.text,' ')
#         print(cards.text)
#     for cards in second_row:
#         title = cards.find('span', class_='element-text')
#     if not title:
#         print('No Card')
#     else:
#         print(title.text,' ')
#         print(cards.text)

# print(divs.text)

# for div in divs:
#     title = div.find('span', class_='element-text')
#     if not title:
#         print('No Card')
#     else:
#         print(title.text,' ')
#         print(div.text)

