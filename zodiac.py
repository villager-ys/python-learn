# 计算星座
a = "鼠牛虎兔龙蛇马羊猴鸡狗猪"
print("牛" in a)
print("猫" not in a)

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座',
               u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
zodiac_day = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
(month, day) = (6, 27)
a = len(list(filter(lambda x: x < (month, day), zodiac_day)))
# print(zodiac_name[a%12])

b_list = ["123", "abc"]
b_list.append(0)
b_list.remove("abc")
print(b_list)

