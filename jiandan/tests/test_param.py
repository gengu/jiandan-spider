__author__ = 'genxiaogu'

def fn1(*c):
    fn2(*c)

def fn2(d,*c):
    print "d => " , d
    print "c => " , c

fn1()