__author__ = 'genxiaogu'

import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class Hotel(object):

    def __init__(self):
        self.file = open('aba.txt','wb')

    def pass_item(self,item,spider):
        if item:
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line.decode('unicode_escape'))
        return item


