__author__ = "Alex Li"

import gevent

def foo():
    print('Running in foo')
    gevent.sleep(2)   # 跳过两次执行
    print('Explicit context switch to foo again')
def bar(n):
    print('Explicit精确的 context内容 to bar')
    gevent.sleep(1)
    print('Implicit context switch back to bar',n)
def func3():
    print("running func3 ")
    gevent.sleep(0)
    print("running func3  again ")


gevent.joinall([
    gevent.spawn(foo), #生成，
    gevent.spawn(bar(11)),
    gevent.spawn(func3),
])