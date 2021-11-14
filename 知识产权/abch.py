import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# 获取各个页面的url（由于各个页面的url类似，可以考虑直接构建）
a_urls_list = ['https://www.cnipa.gov.cn/tjxx/jianbao/year{}/a.html'.format(year) for year in range(2008,2021)]
b_urls_list = ['https://www.cnipa.gov.cn/tjxx/jianbao/year{}/b.html'.format(year) for year in range(2008,2021)]
c_urls_list = ['https://www.cnipa.gov.cn/tjxx/jianbao/year{}/c.html'.format(year) for year in range(2008,2021)]
h_urls_list = ['https://www.cnipa.gov.cn/tjxx/jianbao/year{}/h.html'.format(year) for year in range(2008,2021)]
print(a_urls_list)

# 爬取并存储数据
# 当前目录下创建文件夹，存放爬取的数据
dir_path = './data'
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}


# 下载xlsx文件
def download_source(source_url, output_path):
    print(source_url)
    response = requests.get(url=source_url, headers=headers, stream=False)
    with open(output_path, mode='wb') as f:
        f.write(response.content)


# 对url列表进行调整，删除重复的以及无用的url
# （顺便吐槽一下网站，怎么做的那么不整齐，爬虫都嫌弃）
def list_adjust(a_list):
    n = len(a_list)
    cur_list = []
    for element in a_list:
        if element.split('/')[-1] == 'indexy.html':
            continue
        if element not in cur_list:
            cur_list.append(element)
    return cur_list


#     1. 调用函数 **get_store()** ，传入类型（'a''b''c''d'之一）和该类型的url列表  **[a_urls_list]**。
#     2. 创建该类型的文件夹  **[type_dir_path]**。
def get_store(urls_list, url_type):
    type_dir_path = './data/{}'.format(url_type)
    if not os.path.exists(type_dir_path):
        os.mkdir(type_dir_path)

    #     3. 遍历列表中的每一个url，即该类型每一年的数据。
    for url in urls_list:
        #     4. 对该年数据创建文件夹  **[year_dir_path]**。
        year = url.split('year')[1].split('/')[0]
        year_dir_path = type_dir_path + '/' + year
        if not os.path.exists(year_dir_path):
            os.mkdir(year_dir_path)
        #     5. 访问该url，使用beautiful soup进行页面解析，得到该年该类型的所有数据的url **[detail_list]**。
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        detail_list = [url.split(url_type + '.html')[0] + x['href'] for x in soup.select('.style2 a')]
        # 对列表进行调整
        detail_list = list_adjust(detail_list)
        print(detail_list)

        #     6. 遍历 **[detail_list]** 中的所有url，将url切片用于拼接xls/xlsx的地址，然后将这个拼接的地址和这个xls/xlsx即将存放的位置，一起传入函数 **download_source()** 。
        if year == '2020':
            for detail_url in detail_list:
                download_source(detail_url.split('html')[0] + 'xlsx',
                                year_dir_path + '/' + detail_url.split('/')[-1].split('.')[0] + '.xlsx')
        else:
            for detail_url in detail_list:
                download_source(detail_url.split('html')[0] + 'xls',
                                year_dir_path + '/' + detail_url.split('/')[-1].split('.')[0] + '.xls')

# get_store(a_urls_list,'a')
# get_store(b_urls_list,'b')
get_store(c_urls_list,'c')
# get_store(h_urls_list,'h')