# # 內置函數
# # filter
# a = [1, 2, 3, 4, 5, 6]
# b = list(filter(lambda x: x >= 4, a))
#
# # map
# list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))  # 使用 lambda 匿名函数
# # [1, 4, 9, 16, 25]
#
# # 提供了两个列表，对相同位置的列表数据进行相加
# list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
# # [3, 7, 11, 15, 19]

# # reduce
# from functools import reduce
# d = reduce(lambda x, y: x+y, [1, 2, 3], 1)
# print(d) # 7

# zip
a = (1, 2, 3)
b = [2, 4, 6]
zip(a, b) # 打包成元组列表 [(1, 2),(2, 4),(3, 6)]
for i in zip(a, b):
    print(i)