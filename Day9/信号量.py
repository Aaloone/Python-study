__author__ = "Alex Li"

import threading, time


def run(n):
    semaphore.acquire()    #控制同时允许进行的线程，请求线程
    time.sleep(1)
    print("run the thread: %s\n" % n)
    semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行  进一个出一个
    for i in range(22):
        t = threading.Thread(target=run, args=(i,))
        t.start()
while threading.active_count() != 1:
    # print(threading.active_count())
    pass
else:
    print('----all threads done---')
    #print(num)