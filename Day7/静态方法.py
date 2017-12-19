
import os
# os.system()
# os.mkdir()

class Dog(object):
    def __init__(self,name):
        self.name = name

    @staticmethod #实际上跟类没什么关系了，切断了和类的关联
				  #没有的话，self 不用传参数，有的话 self 需要另外传参数
    def eat(self,job):
        print("%s is eating %s" %(self.name,'dd'))

    def talk(self):
        print("%s is talking"% self.name)
d = Dog("ChenRonghua")
d.eat(d,'t')     # 如果 def eat(self); 有参数，  则调用 eat( )  里面需要传入实例化参数 如果没有参数则不用传入
d.talk()    #  没有@staticmethod  则不考虑