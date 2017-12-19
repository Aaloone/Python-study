__author__ = "Alex Li"


class AlexError(Exception):
    def __init__(self, msg):
        self.message = msg
    def __str__(self):    # 类执行时先执行这一步，然后执行构造函数
        return 'sdfsf'   # 返回值即为赋值给 e 的值，将在异常中显示，若没有定义 return，则返回构造函数中赋予的值
try:
    raise AlexError('数据库连不上')
except AlexError as e:
    print(e)