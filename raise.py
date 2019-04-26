# 异常处理 raise关键字
# try :
#     s = None
#     if s is None:
#         print('s是空对象')
#         raise NameError
#     print(len(s))
# except TypeError:
#     print('空对象没有长度')

try :
    a = open(r'a.txt', 'r')
    a.read()
except Exception as e:
    print(e)
finally:
    a.close()

