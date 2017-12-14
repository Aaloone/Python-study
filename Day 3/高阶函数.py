__author__ = "Alex Li"

def add(a,b,f):    #把函数当作参数传入
    return f(a)+f(b)

res = add(3,-6,abs)
print(res)


