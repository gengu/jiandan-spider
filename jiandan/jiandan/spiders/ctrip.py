__author__ = 'genxiaogu'


# http://hotels.ctrip.com/

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
# from jiandan.jiandan.items.hotel import hotel

from jiandan.items.hotel import *
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class ctrip(CrawlSpider):
    name = "ctrip"
    allowed_domains = ["ctrip.com"]
    start_urls = [
        'http://hotels.ctrip.com/hotel/1684711.html'
    ]
    rules = (
        # track this url
        # Rule(LinkExtractor(allow=('hotels.ctrip.com/hotel/([a-zA-Z0-9]+)/',),deny=('hotels.ctrip.com/hotel/dianping/([0-9]+)\.html',))),
        # get res body
        # Rule(LinkExtractor(allow=('hotels.ctrip.com/hotel/([0-9]+)\.html',),),callback='parse_hotel'),
        # get res body
        Rule(LinkExtractor(allow=('hotels.ctrip.com/hotel/([0-9]+)\.html',),),callback='parse_hotel',process_links=False),
    )

    def parse_hotel(self,res):
        item = hotel()
        item['name'] = res.xpath('//div[@class="name"]/h2[@class="cn_n"]/text()').extract()[0]
        item['url'] = res.url
        # # print '=====>',res.xpath('//span[@class="price"]')
        # # print '=====>',res.xpath('//p[@class="staring_price"]/span[@class="price"]')
        # item['city'] = res.xpath('//div[@class="address"]/span[@id="ctl00_MainContentPlaceHolder_commonHead_lnkCity"]/text()').extract()[0]
        item['city'] = res.xpath('//div[@id="ctl00_MainContentPlaceHolder_commonHead_lnkCity"]/text()').extract()
        item['price'] = res.xpath('//p[@class="staring_price"]/span[@class="price"]/text()').extract()
        #
        # print "name ==== > " , name , "url === > " , res.url
        # return item
        # print item
        # with open('genxiaogu','wb') as f:
        #     f.write(i)
        yield item
        # print res.body

