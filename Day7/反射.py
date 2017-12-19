__author__ = "Alex Li"

def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..."%self.name,food)


d = Dog("NiuHanYang")
choice = input(">>:").strip()

if hasattr(d,choice):    #  判断输入的字符串 是否在类中 包含同名的方法 有则返回 Ture
    a  =  getattr(d,choice)   #  映射返回 类中方法的内存对象  ，如果是 实例属性 的话直接返回结果
    a('dog')     # 调用类的方法
else:
    setattr(d,choice,bulk) # setattr  的作用即   d.talk = bulk
    func = getattr(d, choice)
    func(d)

d.talk(d)    # 调setattr 设置的方法,此处只能在输入是  talk 时才成功，函数 else 中的 func（b）就可以实现这一步骤