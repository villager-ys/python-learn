# 正则表达式
import re

# p = re.compile('...')
# print(p.match('bat'))
# print(r'\nx\n')
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2018-04-26'))
print(p.match('2018-04-26').groups())
year, month, day = p.match('2018-04-26').groups()
print(year)

# findAll()查询所有,返回一个列表
# match 和 search 是匹配一次 findall 匹配所有
print(p.findall('2018-04-26'))


print(p.search('aaa2018-04-26bb'))

print(re.sub(r'c', '*', 'abc'))

phone = '131-2015-4458 #这是某人的手机号码'
print(re.sub(r'#.*$', '', phone))
p2 = re.sub(r'#.*$', '', phone)
print(re.sub(r'\D', '', p2))
