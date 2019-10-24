# 闭包实现 ax+b = y
def a_line(a, b):
    def arg_y(x):
        return a*x+b
    return arg_y

# a = 3,b = 4
line1 = a_line(3, 4)
y = line1(2)
print(y)

# # 装饰器
# import time
#
#
# def timer(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print("运行时间是%s秒" % (end_time - start_time))
#     return wrapper
#
#
# @timer
# def i_sleep():
#     time.sleep(3)

#
# i_sleep()
