
class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students =[]
        self.staffs =[]
    def enroll(self,stu_obj):
        print("为学员%s 办理注册手续"%stu_obj.name )
        self.students.append(stu_obj)
    def hire(self,staff_obj):
        self.staffs.append(staff_obj)
        print("雇佣新员工%s" % staff_obj.name)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

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

class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade
    def tell(self):
        print('''
        ---- info of Student:%s ----
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))
    def pay_tuition(self,amount):    #新的参数，在 pay_tuition(amount) 一定要给 amount 传参数
        print("%s has paid tution for $%s"% (self.name,amount) )


school = School("老男孩IT","沙河")

t1 = Teacher("Oldboy",56,"MF",200000,"Linux")  #实例化一个类
t2 = Teacher("Alex",22,"M",3000,"PythonDevOps")

s1 = Student("ChenRonghua",36,"MF",1001,"PythonDevOps") #实例化一个类
s2 = Student("徐良伟",19,"M",1002,"Linux")


t1.tell()  #调用类的属性
s1.tell()
school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.students)
print(school.staffs)   #列表中存入的是  class Teachers（object）:  实例化的结果 此处返回的是 实例化 地址 组成的列表
school.staffs[0].teach()    #相当于 t1.teach()

for stu in school.students:
    stu.pay_tuition(5000)

print(SchoolMember())