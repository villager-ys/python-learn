# matplotlib曲线库
import numpy as np
import matplotlib.pyplot as plt
plt.plot([1, 5, 9], [4, 6, 10])
plt.show()

x = np.linspace(-np.pi, np.pi, 100)  # x轴定义域为-3.14 ~ 3.14,中间间隔100个元素单位
plt.plot(x, np.sin(x))
# 显示曲线图
plt.show()

# 多曲线图
x = np.linspace(-np.pi * 2, np.pi * 2, 100)  # x轴定义-2pi到2pi
plt.figure(1, dpi=50)  # 创建图表1
for i in range(1, 5):
    plt.plot(x, np.sin(x / i))
plt.show()

# 直方图
plt.figure(1, dpi=50)  # 创建图表1,dpi代表图片精度，dpi越大文件越大，杂志一般需要300精度以上
data = [1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 4]
plt.hist(data)  # hist只需要输入数据，直方图自动统计出现的次数
plt.show()

# 散点图
x = np.arange(1, 10)
y = np.arange(1, 10)
plt.figure(1, dpi=40)
plt.scatter(x, y, c='r', marker='o')  # c = 'r'表示散点的颜色为红色，marker='0'表示散点形状为o型
plt.show()
