from bs4 import BeautifulSoup
import sys 
import pandas as pd
import re 
import requests

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
#$chileno test link: https://store.steampowered.com/search/?sort_by=Price_ASC&maxprice=3000&category1=998%2C996&category2=29&os=win

list_pages = ['https://store.steampowered.com/search/?sort_by=Price_ASC&maxprice=70&category1=998%2C996&category2=29&os=win'
                'https://store.steampowered.com/search/?sort_by=Price_ASC&sort_order=ASC&category1=998%2C996&category2=29&price=%2C70&os=win&maxprice=70&page=2',
                'https://store.steampowered.com/search/?sort_by=Price_ASC&sort_order=ASC&category1=998%2C996&category2=29&price=%2C70&os=win&maxprice=70&page=3',
                'https://store.steampowered.com/search/?sort_by=Price_ASC&sort_order=ASC&category1=998%2C996&category2=29&price=%2C70&os=win&maxprice=70&page=4',
                'https://store.steampowered.com/search/?sort_by=Price_ASC&sort_order=ASC&category1=998%2C996&category2=29&price=%2C70&os=win&maxprice=70&page=5'
                ]
            #    'https://store.steampowered.com/search/?sort_by=Price_ASC&sort_order=ASC&category1=998%2C996&category2=29&price=%2C70&os=win&maxprice=70&page=6',
            #    'https://store.steampowered.com/search/?sort_by=Price_ASC&sort_order=ASC&category1=998%2C996&category2=29&price=%2C70&os=win&maxprice=70&page=7',
            #    'https://store.steampowered.com/search/?sort_by=Price_ASC&sort_order=ASC&category1=998%2C996&category2=29&price=%2C70&os=win&maxprice=70&page=8',
            #    'https://store.steampowered.com/search/?sort_by=Price_ASC&sort_order=ASC&category1=998%2C996&category2=29&price=%2C70&os=win&maxprice=70&page=9',
               
              
games = []
for page in list_pages:
    driver = requests.get(page)
    page = BeautifulSoup(driver.text, 'html.parser')
    links = page.findAll('a', class_='search_result_row ds_collapse_flag app_impression_tracked')
    pages = page.findAll('a')
    
    for page in pages:
        if page.get('href') is not None:
            if 'store.steampowered.com/app/' in page.get('href'):
                appid = page.get('data-ds-appid')
                title = page.find('span', class_='title')
                div = page.find('div' , class_='col search_price discounted responsive_secondrow')
                discount = page.find('div', class_="col search_discount responsive_secondrow")
                discount = (discount.text)
                discount = re.sub('[^0-9]', '', discount)
                div = (div.text).split()
                if "," in appid:
                    games.append((title.text, appid + "es un pack", float(div[2].replace(',', '.')),discount))
                else:
                    games.append((title.text, appid, float(div[2].replace(',', '.')),discount))
                
print(len(games))
df = pd.DataFrame(games, columns=['Title', 'AppID', 'Price', 'Discount'])
print(df)    
df.to_json('games.json', orient='records', indent=4)





#href="https://store.steampowered.com/search/?sort_by=Price_ASC&sort_order=ASC&category1=998%2C996&category2=29&price=%2C70&os=win&maxprice=70&page=2"

