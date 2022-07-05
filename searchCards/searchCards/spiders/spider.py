import json
from urllib import response
import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from searchCards.items import SearchcardsItem
from scrapy.exceptions import CloseSpider
import sys
from searchCards.items import SearchPricesItem

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

class SearchCardsSpider(CrawlSpider):
    prices = []
    name = 'get_prices'
    allowed_domains = ['steamcommunity.com']
    
    def start_requests(self):
        with open('appids.json') as f:
            data = json.load(f)
            for game in data:
                self.prices.clear()
                print(game['game'])
                for card in game['values']:
                    appid = '753'
                    urls = [
                        'https://steamcommunity.com/market/priceoverview/?appid='+appid+'&currency=34&market_hash_name='+str(card).replace('[','').replace(']','').replace("'",'')
                            ]
                    for url in urls:
                        scrapy.Request(url=url, callback=self.parse_item)
                    
                        
#https://steamcommunity.com/market/priceoverview/?appid=753&currency=34&market_hash_name=509920-Gaius%20And%20Girder
    
    def parse_item(self, response):
        jsonresponse = json.loads(response.text)
        self.prices.append(jsonresponse['lowest_price'])
        
        
        
        
        
        
    
  



        
        
        
        