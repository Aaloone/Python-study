# -*- coding= utf-8 -*-
# 继承 在子类中传入参数，然后可以直接调用父类的方法，父类自动获取子类传入的值
# class People: 经典类
#py2 经典类是按深度优先来继承的，新式类是按广度优先来继承的
#py3 经典类和新式类都是统一按广度优先来继承的
class People(object): #新式类
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.friends = []
        print("--doens't run ")
    def eat(self):
        print("%s is eating..." % self.name)
    def talk(self):
        print("%s is talking..." % self.name)
    def sleep(self):
        print("%s is sleeping..." % self.name)

class Relation(object):
    #def __init__(self,n1,n2):	#多继承测试执行顺序 n1,n2 是为接收传入的参数
        #print("init in relation")
    def make_friends(self,obj): # 此处 obj 相当于传入的 w1 ，w1 已经成为实例
        print("%s is making friends with %s" % (self.name,obj.name))  #obj.name = w1.name
        self.friends.append(obj) #不使用 obj.name 是为了传入地址，保证 name(实例变量) 修改后的联动
class Man(Relation,People):
     def __init__(self,name,age,job,money = 100):   # 继承的条件下 添加新的参数
         #People.__init__(self,name,age)   # 经典类继承写法
        super(Man,self).__init__(name,age) #新式类写法   遇到第一个构造函数便停止，如果没有一直向上寻找构造函数
        self.money  = money
        self.job = job
        print("%s 一出生就有%s money" %(self.name,self.money))
     def piao(self):
        print("%s is piaoing ..... 20s....done." % self.name)
     def sleep(self):
        People.sleep(self)
        print("man is sleeping ")
class Woman(People,Relation):	#多继承，执行顺序从左到右
    def get_birth(self):
        print("%s is born a baby...." % self.name)

print("in the func")
m1 = Man("NiuHanYang",22,'it')
print(m1.eat())
w1 = Woman("ChenRonghua",26)
#
m1.make_friends(w1)
w1.name = "陈三炮"
print(m1.friends[0].name)
