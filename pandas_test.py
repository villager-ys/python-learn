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

#dataframe 类似于电子表格的形式
data = {'city': ['上海','杭州','北京'],
        'year':[2017,2018,2019],
        'salary':[3000.4,4008.8,50047.9]}
frame = DataFrame(data)
frame2 = DataFrame(data,columns=['city','salary','year'])
print(frame)
print(frame2)
print(frame2.year)
print(frame2['city'])

# 层次化索引
import numpy as np
data2 = Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],
                                  [1,2,3,1,2,3,1,2,2,4]])
print(data2)
# 转成类似dataframe二维数据
print(data2.unstack())

