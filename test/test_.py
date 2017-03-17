#coding:utf8

'''this is a test module'''

__author__ ='Liu'

import time
import urllib
import json

from PIL import Image

import class_ as cls

def test_fn():
    print 'hello I am a test function'
    #time.sleep(2)


if __name__ == '__main__':
    
    test_fn()

rawData = urllib.urlopen('http://59.110.45.134/')
#jsonData = json.loads(rawData)
#print type(rawData.read())#jsonData

im = Image.open('pand.jpg')
print 'format:', im.format, 'size:', im.size, 'mode:', im.mode

#im.thumbnail((200,200))
#im.save('thum.png','PNG')
#im.show()




class Animal(object):

    def __init__(self, name='cat', age=12):
        self.__name = name      
        self.age = age

    def run(self):
        print 'Animals are running'

class Dog(Animal):

    def run(self):
        print 'dog is running'

def run(animal):
    animal.run()

an = Animal()


        
cls.make_sum().sum_(1,3)
print cls.cheng(3,2)













