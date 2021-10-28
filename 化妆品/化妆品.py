import requests
import json

url1 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

url2 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'

headers1 = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

data1 = {
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'conditionType': '1'
}
all_list = []
for i in range(1,10):
    respond1 = requests.post(url=url1,data=data1,headers=headers1)
    all_list.extend([x for x in respond1.json()['list']])
    # for x in all_list:
    #     print(x)
print('记录数：' + str(len(all_list)))

# detail information
data2 = {
    'id':'7b85196bed6b48b9b73eaa28075a724f'
}

all_info = []
for x in all_list:
    data2['id'] = x['ID']
    respond2 = requests.post(url=url2, data=data2, headers=headers1)
    all_info.append(respond2.json())

print('详细数据条数：'+str(len(all_info)))
# print(all_info)

# 4
for x in all_info:
    print(x['epsName'] + ':' + str(x['epsProductAddress']))
with open('化妆品.json', 'w', encoding='utf-8') as fp1:
    json.dump(all_info,fp=fp1,ensure_ascii=False)
print('保存到”' + '化妆品.json' + '“文件里了捏。')


'''
从首页抓取id，再用id抓取详细信息

'''

