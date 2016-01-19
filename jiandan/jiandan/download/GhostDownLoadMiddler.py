__author__ = 'genxiaogu'


# headless testing platform
from selenium import webdriver
from scrapy.http import HtmlResponse;
import os

class PhantomjsError(Exception):
    pass

class DownloadMiddler(object):
    def __init__(self,driver):
        self.driver = driver
        pass

    @classmethod
    def from_crawler(cls, crawler):
        instance = cls.from_setting(crawler.settings) ;
        return instance

    @classmethod
    def from_setting(cls,settings):
        path = settings.get('PHANTOMJS_PATH','/Users/genxiaogu/GitLab/nvm/v0.11.14/bin/phantomjs')
        if os.path.exists(path):
            pass
        else:
            raise PhantomjsError("phantomjs path not exists")
        phantomjs_conf = settings.get('PHANTOMJS_CONF')
        if phantomjs_conf != '' and phantomjs_conf is not None:
            conf = phantomjs_conf.split(',') ;
        driver = webdriver.PhantomJS(service_args=conf,executable_path=path)
        return cls(driver);


    def process_request(self,request,spider):
        self.driver.get(request.url) ;
        return HtmlResponse(request.url , encoding='utf-8',body=self.driver.page_source.encode('utf-8'));