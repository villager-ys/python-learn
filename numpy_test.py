import numpy as np

arr1 = np.array([2, 4, 8])  # 创建数组
print(arr1)
print(arr1.dtype)

arr2 = np.array([1.2, 2.3, 3])
print(arr2)
print(arr2.dtype)
print(arr1 + arr2)

data = [[1, 2, 3], [4, 5, 6]]  # 矩阵转数组
arr3 = np.array(data)
print(arr3)
print(arr3.dtype)

print(np.zeros(10))  # 创建一行10列 0 矩阵 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(np.zeros((3, 5)))  # 创建三行5列 0 矩阵 [[0. 0. 0. 0. 0.]
#                                             [0. 0. 0. 0. 0.]
#                                             [0. 0. 0. 0. 0.]]
print(np.ones((2, 4)))  # 创建2行4列 1 矩阵 [[1. 1. 1. 1.]
#                                           [1. 1. 1. 1.]]
print(np.empty((3, 2)))  # 创建3行2列 空 矩阵 [[2.11395428e-307 3.44900538e-307]
#                                             [4.00535364e-307 4.45039557e-307]
#                                             [4.67294030e-307 1.89141633e-307]]
arr4 = np.arange(10)  # 创建 0-9数组 [0 1 2 3 4 5 6 7 8 9]
print(arr4)
print(arr4[5:8])
arr4[5:8] = 10
print(arr4)
# 不改变原有数组
arr_slice = arr4[5:8].copy()  # 复制一份
arr_slice[:] = 15
print(arr_slice)
print(arr4)
