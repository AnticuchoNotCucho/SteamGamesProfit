import csv
import json
import scrapy 
import chompjs
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from searchCards.items import SearchcardsItem
from scrapy.exceptions import CloseSpider
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

class SearchCardsSpider(CrawlSpider):
    name = 'get_prices'
    allowed_domains = ['steamcommunity.com']
    
    def start_requests(self):
        with open('appids.json') as f:
            data = json.load(f)
            for game in data:
                for card in game['values']:
                    appid = '753'
                    card = '381870-Piggie'
                    print (card)
                    urls = [
                        'https://steamcommunity.com/market/priceoverview/?appid='+appid+'&currency=34&market_hash_name='+(card)
                            ]
                    for url in urls:
                        yield scrapy.Request(url=url, callback=self.parse_item)
#https://steamcommunity.com/market/priceoverview/?appid=753&currency=34&market_hash_name=509920-Gaius%20And%20Girder

    def parse_item(self, response):
        jsonresponse = json.loads(response.text)
        print(jsonresponse)



        
        
        
        