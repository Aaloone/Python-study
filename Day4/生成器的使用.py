__author__ = "Alex Li"

def fib(max): #10
    n, a, b = 0, 0, 1
    while n < max: #n<10
        #print(b)
        yield b
        a, b = b, a + b
        #a = b     a =1, b=2, a=b , a=2,
        # b = a +b b = 2+2 = 4
        n = n + 1
    return '---done---' #生成器中的 return 函数可以在判断异常时确定要返回的结果，异常返回的消息

f= fib(10)
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

print("---------dddd")
print(f.__next__())
print("======")
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

print("====start loop======")
#for i in f:
#    print(i)

# g: 1
# g: 1
# g: 2
# g: 3
# g: 5
# g: 8
# Generator return value: ---done---   #前面 return 的值
# ---------dddd
# 1
# ======
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
#     print(f.__next__())
# StopIteration: ---done---