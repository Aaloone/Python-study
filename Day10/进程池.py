__author__ = "Alex Li"

from  multiprocessing import Process, Pool,freeze_support
import time
import os

def Foo(i):
    time.sleep(2)
    print("in process",os.getpid())
    return i + 100

def Bar(arg):
    print('-->exec done:', arg,os.getpid())

if __name__ == '__main__':  # 区别主动执行还是当作模块调用
    #freeze_support()
    pool = Pool(processes=3) #允许进程池同时放入5个进程
    print("主进程",os.getpid())
    for i in range(10):
        # pool.apply_async(func=Foo, args=(i,), callback=Bar(11))  # callback=回调 前面执行完之后，执行 callback 后面的函数,加参数限制性回掉函数，
        pool.apply_async(func=Foo, args=(i,), callback= Bar)  # callback=回调 前面执行完之后，执行 callback 后面的函数，
        #pool.apply(func=Foo, args=(i,)) # 串行  一个一个执行，跟每个后面加了  .join() 一样
        #pool.apply_async(func=Foo, args=(i,)) # 并行
    print('end')
    pool.close()
    pool.join() #进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。.join()