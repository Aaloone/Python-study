class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        print('int sd ok')
        pass
    def bouj(self):
        print('测试中')

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print('''
        ---- info of Teacher:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course [%s]" %(self.name,self.course))



T1= Teacher('AA','ADF','ADFASDF','sdfsdf','adfasdfadf') # 继承 在子类中传入参数，然后可以直接调用父类的方法，父类自动获取子类传入的值
T1.tell()      # 子类拥有此方法的话直接调用，没有的话到父类寻找
T1.bouj()      # 可以直接调用 SchoolMember（）的 方法