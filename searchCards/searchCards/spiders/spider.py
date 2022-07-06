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
                print(game['game'])
                for card in game['values']:
                    appid = '753'
                    urls = [
                        'https://steamcommunity.com/market/priceoverview/?appid='+appid+'&currency=34&market_hash_name='+str(card).replace('[','').replace(']','').replace("'",'')
                            ]
                    for url in urls:
                     yield scrapy.Request(url=url, callback=self.parse_item, meta={'game': game['game']})
                    
                        
#https://steamcommunity.com/market/priceoverview/?appid=753&currency=34&market_hash_name=509920-Gaius%20And%20Girder
    
    def parse_item(self, response):
        jsonresponse = json.loads(response.text)
        item = SearchPricesItem()
        item['price'] = jsonresponse['lowest_price']
        item['game'] = response.meta['game']
        yield item
        
        
        
        
        
        
        
    
  



        
        
        
        