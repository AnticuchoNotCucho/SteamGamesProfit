import json
import pandas as pd
import numpy as np
prices = json.load(open('test.json'))
game_prices = []
count = 0
for i in range(len(prices)):
    try:
        print(prices[count]['game'])
        game_reference = prices[count]['game']
        game_prices.append([])
        game_prices[i].append([game_reference])
        for card in prices:
            if card['game'] == game_reference:
                print(card['price'], count)
                game_prices[i].append([card['price']])
                count += 1
        print(game_prices)
    except:
        print('final de la lista')
        break

for game in game_prices:
    print(game)
    print('\n')


        
            
