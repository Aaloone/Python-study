__author__ = "Alex Li"
import os
import sys,time

print(sys.argv)

print(time.localtime())
a=time.localtime()
b = (a=1,)
print(type(a))
print(a.tm_mon)