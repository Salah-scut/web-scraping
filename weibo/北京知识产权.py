import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
from urllib.parse import urlencode
import re
from selenium import webdriver
import json
from datetime import datetime

url = 'https://weibo.com/ajax/statuses/mymblog'

headers = {
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
'cookie': 'SINAGLOBAL=3304570431115.8477.1602167090855; UOR=,,www.baidu.com; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFDVYezhHHcarjhImviqXvp5JpX5KMhUgL.FoM0eh57e0B71KM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNe057eheXeh.N; ALF=1668406661; SSOLoginState=1636870662; SCF=AsKZt4Wv-g4dWe3Dt7FygvzEBsDIHyqOJ2m7ThRlcyqU8xzHWHWR1uL9N56LqUoVodTTvmgCDNOvt4YL0_YxLTc.; SUB=_2A25MlNpWDeRhGeFN61IR8yrMwjuIHXVv4EyerDV8PUNbmtB-LVP3kW9NQITTp1KQ2ob8DswtVF49XmBUoZRBKSQi; XSRF-TOKEN=SZE3uEYNZ3MpG86u7d143Nft; _s_tentry=weibo.com; Apache=1347733253355.3965.1636870672668; ULV=1636870672718:49:13:1:1347733253355.3965.1636870672668:1636804809827; WBPSESS=VKnvVou2Eze_4WdqQ9qLM8BX393-gLHTC-ZBquHcAajXwayTdNEndlQFjL2N8bjse01S06Wwh6ndVDYQJYkN5NmPgq3Yw-r5ViC9Ae6zrYXSsdSZSpMiM2xnxCFdm23zn5him5_We14xqIRvqopfWg==',
'referer': 'https://weibo.com/u/2611704875',
'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'traceparent': '00-72dd343fbcb0fa415950577e36f4f91d-7b35410988a6e102-00',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
'x-requested-with': 'XMLHttpRequest',
'x-xsrf-token': 'SZE3uEYNZ3MpG86u7d143Nft'
}

params = {
    'uid': '2611704875',
    'page': 1,
    'feature': 0
}


data_dict = []

# 截至2021/11/14，北京知识产权共有10962条数据
# 每一页都返回21条微博

for i in range(1,5):
# for i in range(1,int(10962/21)):
    params['page'] = i
    print('尝试获取第{}页信息'.format(i))
    try:
        response = requests.get(url=url, params=params, timeout=30, headers=headers)
        page_text = response.json()
        content_list = page_text['data']['list']
    except:
        print('第{}页获取数据失败'.format(i))
    else:
        for item in content_list:
            time = item['created_at']
            source = item['source']
            text_raw = item['text_raw']
            data_dict.append([text_raw,time,source])
        time.sleep(5)

dataframe = pd.DataFrame(data=data_dict,columns=['text','time','source'])
print(dataframe)

if not os.path.exists('./微博'):
    os.mkdir('./微博')
dataframe.to_excel('./微博/北京知识产权.xlsx',index=False)