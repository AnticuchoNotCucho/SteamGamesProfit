# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from statistics import median
import scrapy


class SearchcardsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #https://steamcommunity.com/market/priceoverview/?appid=753&currency=34&market_hash_name=509920-Gaius%20And%20Girder
    appid = scrapy.Field()
    hash_name = scrapy.Field()
    url = scrapy.Field()
    pass

class SearchPricesItem(scrapy.Item):
    lowestprice = scrapy.Field()
    medianprice = scrapy.Field()
