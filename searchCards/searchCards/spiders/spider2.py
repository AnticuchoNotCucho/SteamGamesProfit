import csv
import scrapy 
import chompjs
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from searchCards.items import SearchPricesItem
from scrapy.exceptions import CloseSpider

# class SearchPricesSpider(CrawlSpider):
#     name = 'searchPrices'
#     item_count = 0
#     allowed_domains = ['steamcommunity.com']
    
#     with open ('outputfile.csv', 'r') as f:
#         csv_reader = csv.DictReader(f)
#         for row in csv_reader:
#             print(row)
#             appid = row['appid']
#             hash_name = row['hash_name']
#             start_urls = ['https://steamcommunity.com/market/priceoverview/?appid='+appid+'&currency=34&market_hash_name='+hash_name]
        
#     rules = (
#         Rule(LinkExtractor(allow=(), restrict_xpaths=('/html/body/div[1]/div[6]/div[1]/div/div')), callback='parse_item', follow=True),
#     )
#     def parse_item(self, response):
#         item = SearchPricesItem()
#         item['lowestprice'] = response.xpath('/html/body/div[1]/div[6]/div[1]/div/div/div/div[5]/div[6]/pre/span/span[2]').get()
#         item['medianprice'] = response.xpath('/html/body/div[1]/div[5]/div[1]/div/div/div/div[5]/div[8]/pre/span/span[2]').get()
#         print(item['lowestprice'])
#         print(item['medianprice'])      
#         yield item 