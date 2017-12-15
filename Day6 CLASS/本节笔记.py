
#
#
# 特性
# class
# object
#
# 封装
# 继承
# 在子类中传入参数，然后可以直接调用父类的方法，父类自动获取子类传入的值
# py2 经典类是按深度优先来继承的，新式类是按广度优先来继承的
# py3 经典类和新式类都是统一按广度优先来继承的
# 多态
# 一种接口，多种实现

# 语法
#
# 调用函数  --》 执行 --》返回结果
#
# r1 = Role.__init__() return x342423
#
# r1 = Role(r1,"Alex","Police","15000")
# r1.name = "Alex"
# r1.role = "Poice"
# r1.money = 15000
继承中 r1.buy_gun()  # Role.buy_gun(r1)
#


# 属性
# 方法
# 类变量的用途? 大家共用的属性 ,节省开销
# class Person:
#     cn = "中国"
#     def __init__(self,name,age,addr,cn="china")
#         self.name = name
#         self.cn = cn
# p1 = Person(name,age ,addr)
# #
# 构造函数
def __init__(self,nane,nann,dnfdnf):
    self.nane=nane
    self.nann=nann
    self.defdnf = dnfdnf

# 析构函数： 在实例释放、销毁的时候自动执行的，通常用于做一些收尾工作， 如关闭一些数据库连接，关闭打开的临时文件
def __del__(self):
    # 函数值

# 私有方法，私有属性
#
# 类变量
# 实例变量


# 封装



