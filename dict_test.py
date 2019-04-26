# 计算1到10所有偶数相乘
# 列表推导式，字典推导式
alist = [i*i for i in range(1, 11) if(i % 2 == 0)]
print(alist)

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座',
               u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
adict = {i: 0 for i in zodiac_name}
print(adict)