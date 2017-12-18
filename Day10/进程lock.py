__author__ = "Alex Li"

from multiprocessing import Process, Lock


def f(l, i):
    #l.acquire()
    print('hello world', i)
    #l.release()


if __name__ == '__main__':
    lock = Lock()   # 保证在屏幕上的打印数据

    for num in range(100):
        Process(target=f, args=(lock, num)).start()