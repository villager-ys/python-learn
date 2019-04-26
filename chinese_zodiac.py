# 计算生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# year = int(input("请输入年份："))
# print("生肖是：" + chinese_zodiac[year % 12])
#
# for cz in chinese_zodiac:
#     print(cz)

for i in range(1, 13):
    print(i)

for year in range(2000, 2020):
    print("%s 年是生肖 %s" %(year, chinese_zodiac[year % 12]))
