__author__ = "Alex Li"

import os
# os.system()
# os.mkdir()

class Dog(object):
    '''这个类是描述狗这个对象的'''

    def __init__(self,name):
        self.name = name
        self.__food = None

    #@staticmethod #实际上跟类没什么关系了
    #@classmethod
    @property #attribute    把一个方法变成静态属性
    def eat(self):
        print("%s is eating %s" %(self.name,self.__food))
    @eat.setter
    def eat(self,food):
        print("set to food:",food)
        self.__food = food
    @eat.deleter
    def eat(self):
        del self.__food
        print("删完了")

    def talk(self):
        print("%s is talking"% self.name)

    def __call__(self, *args, **kwargs):     # 实例化之后再加 括号 即  对象() 或 类()()
        print("running call",args,kwargs)

    def __str__(self):   # 打印时返回 __str__的返回值
        return "<obj:%s>" %self.name

print(Dog.__doc__)  # 打印函数的帮助提示
print(Dog.__dict__) # 打印类里的所有属性，不包括实例属性
d = Dog("ChenRonghua")
print(d)
print(d.__dict__) # 打印所有实例属性，不包括类属性
# d(1,2,3,name=333)

#Dog("ChenRonghua")()
