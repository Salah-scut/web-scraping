import requests
import re
import os

# 生成存放图片的文件夹
dir_path = './bella'
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

url = 'https://space.bilibili.com/2114847153/dynamic?spm_id_from=444.41.0.0'
headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

ex = '<div .*?="" class="img-content" style="background-image: url"//(.*?)@.*?;"; width:.*?"></div>'

page_text = requests.get(url=url,headers=headers).text

pic_url_list = re.findall(ex, page_text, re.S)

print(pic_url_list)