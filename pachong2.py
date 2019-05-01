import gzip
from io import BytesIO
from urllib import request, parse
url = 'http://httpbin.org/post'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "http://httpbin.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
dict = {
    "name": "value"
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url, data=data, headers=headers, method='post')
response = request.urlopen(req)
# print(response.read().decode('utf-8'))
html = response.read()
buff = BytesIO(html)
f = gzip.GzipFile(fileobj=buff)
res = f.read().decode('utf-8')
print(res)
