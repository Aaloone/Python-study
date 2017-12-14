__author__ = "Alex Li"

import time
def consumer(name):
    '''函数里面有yield,就不再是函数，只是一个生成器'''
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

c = consumer("ChenRonghua")
c.__next__()

# b1= "韭菜馅"
# c.send(b1) 给yiield 传值，并运行
# c.__next__()

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了1个包子,分两半!")
        c.send(i)
        c2.send(i)

producer("alex")