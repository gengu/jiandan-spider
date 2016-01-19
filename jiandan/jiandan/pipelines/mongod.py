__author__ = 'genxiaogu'

from pymongo import MongoClient
from scrapy import  log

import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class Hotel(object):
    def __init__(self,mongo_host,mongo_port,mongo_db):
        try:
            self.client = MongoClient(host=mongo_host,port=mongo_port)
            self.mongo_db = self.client[mongo_db]
        except Exception as e:
            log.ERROR(e)

    @classmethod
    def from_settings(cls, settings,mongo_db=''):
        mongo_host = settings.get('MONGODB_HOST','localhost')
        mongo_port = settings.get('MONGODB_PORT','27017')
        mongo_db = settings.get('MONGODB_DB',mongo_db)
        return cls(mongo_host,mongo_port,mongo_db)

    @classmethod
    def from_crawler(cls,crawler):
        return cls.from_settings(crawler.settings ,crawler.spider.name)

    def proecss_item(self,item,spider):
        if item:
            line = json.dumps(dict(item)) + "\n"
            id = self.mongo_db['hotel'].insert(line) ;
            print 'id ==== > ', id



