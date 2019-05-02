# BeautifulSoup库
from bs4 import BeautifulSoup as bs
html_doc = """
<html>
    <head>
        <title>这是个标题</title>
    </head>
    <body>
        <h1>这是一个一个简单的HTML</h1>
        <p class="hahaha">Hello World！</p>
        <a href="www.baidu.com">1</a>
        <a href="www.baidu.com">2</a>
    </body>
</html>
"""

soup = bs(html_doc, 'lxml')
# 输出标准的html格式
print(soup.prettify())
# 找到title标签
print(soup.title)
# 获取title标签里的内容
print(soup.title.string)
# 获取p标签
print(soup.p)
# 获取p标签class的名字
print(soup.p['class'])
# 获取第一个a标签
print(soup.a)
# 获取所有的a标签
print(soup.find_all('a'))