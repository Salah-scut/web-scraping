'''
如果有使用服务器代理，需要将代理关掉，否则可能报错：ValueError: check_hostname requires server_hostname
'''

import json
import requests

# 1
url1 = 'https://fanyi.baidu.com/sug'
headers1 = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Host':'fanyi.baidu.com'
}
data1 = {
    'kw': ''
}
data1['kw'] = input()

# 2
respond = requests.post(url=url1,headers=headers1,data=data1)
# 3
fanyi_list = [i for i in respond.json()['data']]

# 4
for x in fanyi_list:
    print(x)
with open('./' + data1['kw'] + '.json','w',encoding='utf-8') as fp1:
    json.dump(fanyi_list,fp=fp1,ensure_ascii=False)
print('保存到”' + data1['kw'] + '.json' + '“文件里了捏。')
