__author__ = "Alex Li"


class Foo(object):
    def __init__(self):
        self.data = {}
    def __getitem__(self, key): # 相当于添加了一个字典
        print('__getitem__', key)
        return self.data.get(key)
    def __setitem__(self, key, value):
        print('__setitem__', key, value)
        self.data[key] =value
    def __delitem__(self, key):
        print('__delitem__', key)


obj = Foo()
obj['name'] = "alex"
# print(obj['name'])
print(obj.data,obj.data['name'],obj['name']) # 后两个返回一样的结果
del obj["sdfdsf"]
result = obj['k1']  # 自动触发执行 __getitem__   和 obj.data['name'] 作用一样
# obj['k2'] = 'alex'  # 自动触发执行 __setitem__
# del obj['k1']