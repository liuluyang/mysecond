#coding:utf8
import unittest


global_num = 2

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

#if __name__ == '__main__':
    #unittest.main()


def sum(x, y):
    return x + y
def sub(x, y):
    return x - y


class mytest(unittest.TestCase):
    #def setUp(self):
        #pass
    #def tearDown(self):
        #pass
    def test_sum(self):
        self.assertEqual(sum(1,2),3,'test sum fail')
    def test_sub(self):
        self.assertEqual(sub(2,1),1,'test sub fail')

class MyClass:
    def __init__(self):
        pass
    def sum_c(self, x, y):
        return x + y

class mytest_c(unittest.TestCase):
    #初始化工作
    def setUp(self):
        self.tclass=MyClass()
    #推出清理工作    
    def tearDown(self):
        pass
    def testsum_c(self):
        self.assertEqual(self.tclass.sum_c(1,3),4)

        
    

str_ = []
if str_:
    print '1'
else:
    print '2'

if __name__=='__main__':
    unittest.main()



