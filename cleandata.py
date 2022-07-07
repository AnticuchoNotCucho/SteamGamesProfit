from distutils.command.clean import clean
import json
from statistics import mean
from turtle import title
import pandas as pd
import numpy as np
prices = json.load(open('test.json'))
game_prices = []
clean_prices = []
count = 0

for i in range(len(prices)):
    try:
        print(prices[count]['game'])
        game_reference = prices[count]['game']
        game_prices.append([])
        game_prices[i].append([game_reference])
        for card in prices:
            if card['game'] == game_reference:
                game_prices[i].append([card['price']])
                count += 1
    except:
        print('final de la lista')
        break
    
for game in game_prices:
    clean_game = []
    for i in range(len(game)):
        if i == 0:
            continue
        clean_value=(str(game[i]).replace('[','').replace(']','').replace("'",'').replace('ARS$','').replace(',','.'))
        clean_game.append(float(clean_value))
    array = np.array(clean_game)
    mean_profit = (np.mean(array)*(len(array)/2)).round(2)
    value = 6.75
    clean_prices.append((game[0],mean_profit,value,(mean_profit-value).round(2)))
df = pd.DataFrame(clean_prices, columns=['Game','MeanValue','GamePrice','Profit'])
print(df)
df.to_csv('Values.csv', index=False)
# array = np.array(price_list)
        # array = array.astype(float)
        # print(array)
        # mean = np.mean(array)*(amount_cards/2)
        # mean = mean * 124
        # profit = mean - game['Price']
        # mean_values.append((game['Title'],np.round(mean, 2), game['Price'],game['Discount'],np.round(profit,2)))           
