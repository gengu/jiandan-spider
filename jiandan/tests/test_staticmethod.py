__author__ = 'genxiaogu'


class C:
    x = 1
    def test(self):
        C.x = 1
    def add(self):
        C.x = C.x + 1
    @classmethod
    def getX(cls):
        return cls.x

if __name__ == "__main__":
    c = C()
    c.add()
    print C.getX()
    print c.getX()