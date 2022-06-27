import json
from bs4 import BeautifulSoup
import sys
import pandas as pd
import re
import requests
import numpy as np

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

games_json = json.load(open('games.json'))
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
                    price_list.append((price))

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
                    price_list.append((price))

            for cards in second_row:
                title = cards.find('span', class_='element-text')
                price = cards.find('a', class_='button-blue')
                if not title:
                    break
                else:
                    price = price.text
                    price = re.findall(r'[\d\.\d]+', price)
                    price = price[0]
                    price_list.append((price))

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
                    price_list.append((price))
            for cards in second_row:
                title = cards.find('span', class_='element-text')
                price = cards.find('a', class_='button-blue')
                if not title:
                    break
                else:
                    price = price.text
                    price = re.findall(r'[\d\.\d]+', price)
                    price = price[0]
                    price_list.append((price))

            for cards in third_row:
                title = cards.find('span', class_='element-text')
                price = cards.find('a', class_='button-blue')
                if not title:
                    break
                else:
                    price = price.text
                    price = re.findall(r'[\d\.\d]+', price)
                    price = price[0]
                    price_list.append((price))
        array = np.array(price_list)
        array = array.astype(float)
        print(array)
        mean = np.mean(array)*(amount_cards/2)
        mean = mean * 124
        profit = game['Price']
        mean_values.append((game['Title'],np.round(mean, 2), game['Price'],game['discount']))
    else: 
        mean_values.append((game['Title'], "No info"))

df = pd.DataFrame(mean_values, columns=['Game','MeanValue','GamePrice','MeanProfit'])
df.to_json('Values.json', orient='records', indent=2)
print(df)
