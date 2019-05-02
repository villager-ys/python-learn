# 爬虫下载图片
from bs4 import BeautifulSoup
import requests as req
import os
import shutil
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "http://httpbin.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}
url = 'https://www.infoq.com/presentations'
# 获取网页图片


def get_image(url):
    response = req.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    # print(soup.find_all('img'))
    dir_path = r'C:\Users\yuanshuai\Desktop\下载图片'
    os.mkdir(dir_path)
    for i in soup.find_all('img'):
        img_url = i.get("src")
        # 等价于 https://www.infoq.com/presentations/a.jpg 取出a.jpg作为file_name
        fire_name = os.path.basename(img_url)
        image_path = os.path.join(dir_path, fire_name)
        download_image(img_url, image_path)

# 下载图片


def download_image(img_url, image_path):
    # 打开流获取下载
    response = req.get(img_url, stream=True)
    if response.status_code == 200:
        with open(image_path, 'wb') as f:
            # 要使用response.raw文件样对象，默认情况下不会解码压缩的响应(使用GZIP或deflate)。
            # 你可以强制它解压缩你设置decode_content属性为True(请求设置为False以控制解码本身)。
            response.raw.decode_content = True
            # 将数据流传输到文件对象
            shutil.copyfileobj(response.raw, f)


get_image(url)
