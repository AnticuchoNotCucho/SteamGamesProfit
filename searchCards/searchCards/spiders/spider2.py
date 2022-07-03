import csv
import json
import scrapy 
import chompjs
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
import sys
from searchCards.items import SearchcardsItem

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

class SearchCardsSpider(CrawlSpider):
    name = 'get_cards'
    allowed_domains = ['steamcommunity.com','steamcardexchange.net']
        
    def start_requests(self):
        with open('games.json') as f:
            data = json.load(f)  
            for game in data:
                urls = [
                    'https://www.steamcardexchange.net/index.php?gamepage-appid-'+game['AppID']
                ]
                for url in urls:
                    yield scrapy.Request(url=url, callback=self.parse, meta={'game': game})
            
    def parse(self, response):
        links = response.xpath('//*[@id="content-area"]/div[2]/div[4]//div[@class="showcase-element"]/div/a/@href').getall()
        list_hash_name = []
        for link in links: #list of hash_name
            link = link.replace('https://steamcommunity.com/market/listings/','')
            hash_name = (link[link.find('/'):len(link)])
            appid = link.replace(hash_name,'')
            hash_name = hash_name.replace('/','')
            # x = hash_name[hash_name.find('-'):len(hash_name)]
            # gameid = hash_name.replace(x,'')
            list_hash_name.append([hash_name])
            print(response.meta['game']['Title'])
        item = SearchcardsItem()
        item['appid'] = appid
        item['values'] = list_hash_name
        item['game'] = response.meta['game']['Title']
        yield item 
        list_hash_name.clear()
            
    
       # //*[@id="content-area"]/div[2]/div[4]//div[@class="showcase-element"]//div//a//@href
        #xpath   https://www.steamcardexchange.net/index.php?gamepage-appid-1334590.get()
        
        #https://steamcommunity.com/market/priceoverview/?appid=753&currency=34&market_hash_name=509920-Gaius%20And%20Girder