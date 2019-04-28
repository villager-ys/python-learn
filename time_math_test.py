# 时间日期test

import time
import datetime

print(time.time())  # 当前时间戳
time.sleep(2)  # 休眠2秒
print(time.localtime())  # 格式化时间戳为本地时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 指定格式格式化时间 返回字符串

# 计算日期相加相减
print(datetime.datetime.now())
new_datetime = datetime.timedelta(minutes=10)  # 日期偏移量
print(datetime.datetime.now() + new_datetime)

one_day = datetime.datetime(2019, 4, 28)
new_datetime = datetime.timedelta(days=10)
print(one_day + new_datetime)

# 随机
import random
print(random.randint(1, 5))
print(random.choice(['aa', 'bb', 'cc']))
