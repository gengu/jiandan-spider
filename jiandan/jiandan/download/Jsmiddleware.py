__author__ = 'genxiaogu'


from tornado import *
# self.browser = webdriver.PhantomJS(executable_path="/usr/local/lib/python2.7/site-packages/selenium/webdriver/phantomjs/")

from selenium import webdriver
service_args = [
    '--load-images=false',
    '--disk-cache=true',
    ]
dr = webdriver.PhantomJS(service_args=service_args)
# dr = webdriver.PhantomJS(executable_path="/Users/genxiaogu/GitLab/nvm/v0.11.14/lib/node_modules/phantomjs/bin/phantomjs")
# dr.get('https://www.baidu.com')
# dr = webdriver.Remote(command_executor="http://localhost:8888/wd/hub")
# # print dr.title
# # print dr.current_url
dr.get('http://hotels.ctrip.com/hotel/1535565.html')
dr.set_page_load_timeout(10)
print dr.title


price = dr.find_element_by_xpath('//div[@id="div_minprice"]/p[@class="staring_price"]/span[@class="price"]').text
print price
with open('hotel.html','wb') as f:
    f.write(dr.page_source.encode('utf-8'))
# print dr.page_source.encode('utf-8')
# print dr.current_url

# dr.quit()
dr.close()
