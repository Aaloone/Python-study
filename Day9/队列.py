__author__ = "Alex Li"

import queue     # 一个萝卜一个坑，放入一个多一个，取走一个少一个

q = queue.PriorityQueue()  #设置优先级

q.put((-1,"chenronghua"))
q.put((3,"hanyang"))
q.put((10,"alex"))
q.put((6,"wangsen"))

print(q.get())
print(q.get())
print(q.get())
print(q.get())


# q  = queue.LifoQueue()
#
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())

