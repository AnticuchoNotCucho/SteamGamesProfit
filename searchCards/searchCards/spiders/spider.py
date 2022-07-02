import csv
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
    name = 'searchCards'
    item_count = 0
    allowed_domains = ['steamcommunity.com','steamcardexchange.net']
    start_urls = ['https://www.steamcardexchange.net/index.php?gamepage-appid-1334590']
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths='//*[@id="content-area"]/div[2]/div[4]'), callback='parse_item', follow=True),
    )
#https://steamcommunity.com/market/priceoverview/?appid=753&currency=34&market_hash_name=509920-Gaius%20And%20Girder

    def parse_item(self, response):
        item = SearchcardsItem() 
        response  = response.xpath('//*[@id="responsive_page_template_content"]/script[2]/text()').get()
        StrA = "".join(response)     
        #print(StrA)
        item['appid'] = ((StrA[(StrA.find('"',StrA.index('appid')))+1:(StrA.find(',',(StrA.find('"',StrA.index('appid')))))]).replace('"','')).replace(':','')
        print(item['appid'])
        item['hash_name'] = ((StrA[(StrA.find('"',StrA.index('market_hash_name')))+1:(StrA.find(',',(StrA.find('"',StrA.index('market_hash_name')))))]).replace('"','')).replace(':','')
        print(item['hash_name'])
        item['url'] = 'https://steamcommunity.com/market/priceoverview/?appid='+item['appid']+'&currency=34&market_hash_name='+item['hash_name']
        print(item['url'])
        yield item

    def parse_next(self, response):
        next_page = response.xpath('//a[@class="market_paging_button_inactive"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_item)
        else:
            raise CloseSpider('No more pages')


        
        
        
        