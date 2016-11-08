#coding:utf-8

"""
class内に初期化しなくてもself変数を追加できるか検証
super
"""

class Test(object):
    def __init__(self):
        self.a = 1
        self.b = 2

    def add_value(self,c):
        self.c = c

    def sum_value(self):
        return self.a + self.b + self.c

class SubTest(Test):
    def __init__(self):
        super(SubTest,self).__init__()

    def sum_value(self):
        return self.a + self.b
        
class InitTest(object):
    def __init__(self,a=1,b=2):
        self.a = a
        self.b = b
    def sum_value(self):
        return self.a + self.b

class InitSubTest(InitTest):
    def __init__(self,*args,**kargs):
        super(InitSubTest,self).__init__(**kargs)
    def sum_value(self):
        return self.a+self.b+10
    
        
def test1():
    test = Test()
    test.add_value(10)
    print test.sum_value()

def test2():
    test = SubTest()
    print test.a

def test3():
    test = InitSubTest(a=2,b=3)
    print test.sum_value()
    
if __name__=="__main__":
    test3()
