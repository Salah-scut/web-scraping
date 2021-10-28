import requests
import re
import os

# 生成用于存放糗图的文件夹
dir_path = './qiutuLibs'
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

url = 'https://www.qiushibaike.com/imgrank/'
headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

# 用通用爬虫对url对应的一整张页面进行爬取
page_text = requests.get(url=url, headers=headers).text

# 用聚焦爬虫对页面进行解析
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
img_url_list = re.findall(ex,page_text,re.S)    # re.S单行匹配，re.m多行匹配

# 遍历url列表
for src in img_url_list:
    # 拼接完整url
    src = 'https:' + src
    # 发起请求
    img_data = requests.get(url=src, headers=headers).content
    # 获得图片名称
    img_name = src.split('/')[-1]
    # 存放位置
    img_path = dir_path + '/' +img_name
    # 保存到本地
    with open(img_path, 'wb') as fp:
        fp.write(img_data)
        print(img_name,'下载成功')