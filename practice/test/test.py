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

'''

class Apple(object):
    name = 'apple'

p1 = Apple()
p2 = Apple()
p1.name = 'orange'
print(p1.name)
print(p2.name)
