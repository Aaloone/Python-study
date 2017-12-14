__author__ = "Alex Li"
import json

f = open("test.text","r")

# data = json.loads(f.read()) #data = pickle.loads(f.read())  可以 dumps 好多次，但是 dumps 多次的结果不能被load出来
# print(data)

for line in f.readline():
    print(json.loads(line))

