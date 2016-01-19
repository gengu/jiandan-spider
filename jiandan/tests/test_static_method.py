__author__ = 'genxiaogu'


IND = 'c'
class C(object):
    def __init__(self, data):
        self.data = data
    # 如果这里的checkC函数没有self参数，那么 @staticmethod
    # 否则 加self参数
    def checkC(self):
        return (IND == 'c')
    def do_reset(self):
        if self.checkC():
            print('do_reset :', self.data)
    def set_db(self):
        if self.checkC():
            self.db = 'hhh'
        print('set_db : ', self.data)

if __name__ == "__main__":
    ik1 = C(12)
    ik1.do_reset()
    ik1.set_db()