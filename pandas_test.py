import pandas as pd
from pandas import Series, DataFrame
# pandas 对一维数组操作 Series
obj = Series([4, 5, -7])
print(obj)
print(obj.index)
print(obj.values)

obj2 = Series([1, 2, 3, -9], index=['a', 'b', 'c', 'd'])
print(obj2)
obj2['d'] = -20
print(obj2)
print('b' in obj2)

a_dict = {'hangzhou': 87000, 'nanjing': 9123, 'beijing': 2231}
obj3 = Series(a_dict)
print(obj3)
# 更换obj3的index
obj3.index = {'hz', 'nj', 'bj'}
print(obj3)
