#coding:utf8
import linecache
from datetime import datetime
import functools
import sys
'''
自定义取绝对值的函数
'''

def my_abs(num):
    
    if not isinstance(num, (int, float)):
        raise TypeError('参数类型不正确')

    if num >= 0:
        return num
    
    else:
        return -num

print my_abs(-3)

'''
必选参数 

默认参数 一定要用不可变对象

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。
'''
def power(x, n=2):
    '''
    计算某数的n次方
    '''
    s = 1
    while n > 0:        
        n = n-1
        s = s*x
        
    return s

print power(3,3)

#n!
def fact(num):
    if num == 1:
        return 1
    if num < 0:
        return 'hehe'
    return num * fact(num - 1)

#文件读取
def read_txt(path):
    for index, one_per in enumerate(open(path,'r').readlines()):
        if index==806:
            print one_per

    #print linecache.getlines(path)        

read_txt('.\pep8-.txt')    

#map函数列表处理    
def change_str(str_):
    one_step = str_.lower()
    return one_step.capitalize()

print change_str('lEw')

List = ['dEw','FGF']
print map(change_str,List)

#列表求积
def cj(x, y):
    return x * y

print reduce(cj, [2,3,4])

#素数筛选
def  fn(x):
    count = 0
    for i in range(1,x+1):
        if x % i == 0:
            count += 1
    if count == 2:
        return True
    else:        
        return False

print filter(fn, range(1,101))


#返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


#装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        kw.setdefault('1','5')
        print ('this func name is %s')%func.__name__
        return func(*args, **kw)

    return wrapper

@log
def now(num, *args, **kw):
    print args
    print kw['1']
    print str(datetime.now())[:-num]



def foo(s):
    return 104 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        result = bar('34')
        print result
    except StandardError, e:
        print 'Error!',e
    finally:
        print 'finally...'

   














    
    







