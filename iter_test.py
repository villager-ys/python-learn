# 迭代器测试

# a_list = [1, 2, 3]
# for i in iter(a_list):
#     print(i)
#
# for i in a_list:
#     print(i)

# # range函数
# range(10)        # 从 0 开始到 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(1, 11)     # 从 1 开始到 11
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# range(0, 30, 5)  # 步长为 5
# [0, 5, 10, 15, 20, 25]
# range(0, 10, 3)  # 步长为 3
# [0, 3, 6, 9]
# range(0, -10, -1) # 负数
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
# range(0)
# []
# range(1, 0)
# []

# # 自定义range函数
# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x += step
#
# for i in frange(1, 10 ,0.5):
#     print(i)

# lambda表达式

def add(x, y):
    return x + y
lambda x, y: x + y
print(add(3, 4))
