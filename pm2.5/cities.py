import requests
from lxml import etree


url = 'https://www.aqistudy.cn/historydata/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

page_text = requests.get(url=url,headers=headers).text

tree = etree.HTML(page_text)

# 解析热门城市
hot_li_list = tree.xpath("//div[@class='bottom']/ul/li")
hot_cities_names = [li.xpath("./a/text()")[0] for li in hot_li_list]
print(hot_cities_names)

# 解析所有城市
all_cities_list = tree.xpath("//div[@class='bottom']/ul/div[2]/li")
all_cities_names = [li.xpath("./a/text()")[0] for li in all_cities_list]
print(all_cities_names)

# result = hot_cities_names.extend(all_cities_names)
# # print(len(result))
# print(hot_cities_names)