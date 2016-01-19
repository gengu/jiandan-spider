__author__ = 'genxiaogu'

from scrapy.item import Item, Field

class hotel(Item):
    name = Field()
    url = Field()
    price = Field()
    city = Field()
