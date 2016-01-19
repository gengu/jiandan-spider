__author__ = 'genxiaogu'
#
#
class C():
    def __init__(self):
        self.x = 'genxio'
    @property
    def x(self):
        return self.x
    @x.setter
    def x(self,y):
        print y
        self.x = y
if __name__ == "__main__":
    c = C()
    # c.setX('ddddd')
    c.x = 'dddd';
    print c.x


# class C:
#     def __init__(self):
#         self.__x=None
#     @property
#     def x(self):
#         return self.__x
#     @x.setter
#     def x(self,value):
#         self.__x=value
#     @x.deleter
#     def x(self):
#         del self.__x
# if __name__ == "__main__":
#     c = C()
#     c.x = 100
#     # c.
#     print c.x