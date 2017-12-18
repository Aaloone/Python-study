__author__ = "Alex Li"

from multiprocessing import Process, Queue
import threading
#import queue

# def f(q):
#     q.put([42, None, 'hello'])

def f(qq):
    print("in child:",qq.qsize())
    qq.put([42, None, 'hello'])

if __name__ == '__main__':
    q = Queue()        #  多进程中的  Queue ，不是导入的 import queue，
    q.put("test123")
    #p = threading.Thread(target=f,)  线程，主线程和子线程可以数据共享。
    p = Process(target=f, args=(q,))  # 进程，主进程不能访问子进程数据，不同的内存
    p.start()
    p.join()
    print("444",q.get_nowait())
    print("444",q.get_nowait())
     # prints "[42, None, 'hello']"
    #print(q.get())  # prints "[42, None, 'hello']"