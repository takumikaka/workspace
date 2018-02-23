# -*- coding: utf-8 -*-

'''
class A(object):
    def foo(self, x):
        print("execuiting foo(%s, %s)" % (self, x))
        print("self", self)
    @classmethod
    def class_foo(cls, x):
        print("execuiting class_foo(%s, %s)" % (cls, x))
        print("cls", cls)
    @staticmethod
    def static_foo(x):
        print("execuiting static_foo(%s)" % x)

a = A()
print(a.foo(1))
print(a.class_foo(1))
print(a.static_foo(1))

###################################################################

#迭代器
print("for x in iter([1, 2, 3, 4]):")
for x in iter([1, 2, 3, 4]):
    print(x)

#生成器
def myyield(n):
    while n>0:
        print("开始生成...")
        yield(n)
        print("生成一次...")
        n -= 1

for i in myyield(4):
    print("遍历得到的值: ", i)

#####################################################################

def delay_fun(x, y):
    def caculator():
        return x+y
    return caculator

print("返回一个求和函数，但并不求和...")
msum = delay_fun(3, 4)
print("调用并求和...")
print(msum())

#####################################################################

class duck(object):
    def walk(self):
        print("I'm duck, I can walk....")
    def swim(self):
        print("I'm duck, I can swim....")
    def call(self):
        print("I'm duck, I can call....")

duck1 = duck()
print(duck1.walk())
print(duck1.swim())
print(duck1.call())

#######################################################################

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("Score must be intager.")
        if value < 0 or value > 100:
            raise ValueError("Score must between 0~100.")
        self._score = value

s = Student()
s.score=60
print(s.score)
s.score=999
print(s.score)

##########################################################################

class Apple(object):
    name = 'apple'

p1 = Apple()
p2 = Apple()
p1.name = 'orange'
print(p1.name)
print(p2.name)

############################################################################

import ssl
import urllib.request
import os
from bs4 import BeautifulSoup

def write_file(html):
    file = open("test.html", "wb")
    file.write(html)
    file.close()

context = ssl._create_unverified_context()
url = "https://cd.lianjia.com/ershoufang/rs%E9%94%A6%E6%B1%9F%E5%9F%8E%E5%B8%82%E8%8A%B1%E5%9B%AD%E4%B8%89%E6%9C%9F/"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request, context=context)
html = response.read()
#print(html.decode("utf-8"))
soup = BeautifulSoup(html, 'lxml')
print(type(soup))
file = write_file(html)
tag = soup.body
#print(tag)

##############################################################################

str = 'jinjiang'
for num in range(1, 10):
    url = "https://cd.lianjia.com/ershoufang/{0}/pg{1}/".format(str, num)
    print(url)

###############################################################################

'''

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import json

data = pd.DataFrame(json.loads(open('/Users/a/Desktop/workspace/practice/lianjia/bodys.json', 'r+').read()))
plt.imshow(data)
plt.show()
