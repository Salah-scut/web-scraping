import requests
from lxml import etree

url = 'https://bj.58.com/ershoufang/'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

page_text = requests.get(url=url, headers=headers).text


tree = etree.HTML(page_text)
div_list = tree.xpath("//section[@class='list']/div")