import json
from bs4 import BeautifulSoup
import sys
import pandas as pd
import re
import requests
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

games_json = json.load(open('games copy.json'))
mean_values = []

for game in games_json:
    price_list = []
    appid = game['AppID']
    url = "https://www.steamcardexchange.net/index.php?gamepage-appid-"+appid
    driver = requests.get(url)
    page = BeautifulSoup(driver.text, 'html.parser')
    if page.find('div', class_="game-title"):
        first_row = page.find('div', class_='showcase-element-container card')
        second_row = first_row.find_next(
            'div', class_='showcase-element-container card')
        third_row = second_row.find_next(
            'div', class_='showcase-element-container card')
        amount_cards = first_row.find('span', class_='element-count')
        amount_cards = amount_cards.text
        amount_cards = amount_cards.split()
        amount_cards = int(amount_cards[3])
        print(game['Title'], game['AppID'], amount_cards)
        if amount_cards <= 6:
            for cards in first_row:
                title = cards.find('span', class_='element-text')
                price = cards.find('a', class_='button-blue')
                if not title:
                    break
                else:
                    price = price.text
                    price = re.findall(r'[\d\.\d]+', price)
                    price = price[0]
                    price_list.append((title.text,price))

        if amount_cards > 6 and amount_cards <= 12:

            second_row = first_row.find_next(
                'div', class_='showcase-element-container card')

            for cards in first_row:
                title = cards.find('span', class_='element-text')
                price = cards.find('a', class_='button-blue')

                if not title:
                    break
                else:
                    price = price.text
                    price = re.findall(r'[\d\.\d]+', price)
                    price = price[0]
                    price_list.append((title.text,price))

            for cards in second_row:
                title = cards.find('span', class_='element-text')
                price = cards.find('a', class_='button-blue')
                if not title:
                    break
                else:
                    price = price.text
                    price = re.findall(r'[\d\.\d]+', price)
                    price = price[0]
                    price_list.append((title.text,price))

        elif amount_cards > 12 and amount_cards <= 18:
            second_row = first_row.find_next(
                'div', class_='showcase-element-container card')
            third_row = second_row.find_next(
                'div', class_='showcase-element-container card')
            for cards in first_row:
                title = cards.find('span', class_='element-text')
                price = cards.find('a', class_='button-blue')
                if not title:
                    break
                else:
                    price = price.text
                    price = re.findall(r'[\d\.\d]+', price)
                    price = price[0]
                    price_list.append((title.text,price))
            for cards in second_row:
                title = cards.find('span', class_='element-text')
                price = cards.find('a', class_='button-blue')
                if not title:
                    break
                else:
                    price = price.text
                    price = re.findall(r'[\d\.\d]+', price)
                    price = price[0]
                    price_list.append((title.text,price))

            for cards in third_row:
                title = cards.find('span', class_='element-text')
                price = cards.find('a', class_='button-blue')
                if not title:
                    break
                else:
                    price = price.text
                    price = re.findall(r'[\d\.\d]+', price)
                    price = price[0]
                    price_list.append((title.text,price))
        for title in price_list:
            print(title[0])
            get_title = requests.get('https://steamcommunity.com/market/search?q='+title[0], headers={'User-Agent': 'OperaGx/28.0'})
            soup = BeautifulSoup(get_title.text, 'html.parser')
            price = soup.find('span', class_='normal_price')
            print(price.text)
            
        # array = np.array(price_list)
        # array = array.astype(float)
        # print(array)
        # mean = np.mean(array)*(amount_cards/2)
        # mean = mean * 124
        # profit = mean - game['Price']
        # mean_values.append((game['Title'],np.round(mean, 2), game['Price'],game['Discount'],np.round(profit,2)))
    else: 
        mean_values.append((game['Title'], "No info"))

df = pd.DataFrame(mean_values, columns=['Game','MeanValue','GamePrice','Discount','Profit'])
df.to_json('Values.json', orient='records', indent=2)
df.to_csv('Values.csv', index=False)
print(df)


#https://steamcommunity.com/market/priceoverview/?appid=753&currency=34&market_hash_name=509920-Gaius%20And%20Girder