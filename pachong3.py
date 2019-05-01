# requests库
# import requests as req
# # get请求
# url = 'http://httpbin.org/get'
# data = {"key": "value", "abc": "xyz"}
# response = req.get(url, data)
# print(response.text)
#
# # post请求
# url = 'http://httpbin.org/post'
# response = req.post(url, data)
# print(response.text)

# requests结合re正则
import requests as req
import re
context = req.get("http://www.cnu.cc/discoveryPage/hot-人像").text
# print(context)

# <div class="grid-item work-thumbnail">
# <a href="http://www.cnu.cc/works/351070" class="thumbnail" target="_blank">
# <div class="title">"广州森林“</div>
# <div class="author>安正</div>
# <img src="http://img.cnu.cc/uploads/images/flow/1904/26/b0bb0ccad62b3b1992f4d4249433c528.jpg?width=2983&amp;height=1678" alt=""广州森林“">
# </a>

# <div class="grid-item work-thumbnail">
# <a href="(.*？)" .*?title">(.*?)</div>
# <div class="author>安正</div>
# <img src="http://img.cnu.cc/uploads/images/flow/1904/26/b0bb0ccad62b3b1992f4d4249433c528.jpg?width=2983&amp;height=1678" alt=""广州森林“">
# </a>

pattern = re.compile(r'<a href="(.*?)" .*?title">(.*?)</div>', re.S)
results = re.findall(pattern, context)
print(results)
for result in results:
    url, name = result
    # 替换 '\s'匹配空白
    print(url, re.sub(r'\s', '', name))
