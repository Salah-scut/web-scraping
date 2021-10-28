import requests
from pandas import DataFrame

#1.指定url
url1 = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}
params = {
    'cname': '广州',
    'pid': '',
    'pageIndex': '1',
    'pageSize': '100'
}

#2.发起请求
result = []     #用于存放门店记录
for i in range(1,4):
    # 把总共294家KFC门店分成了3页，每页最多展示100家门店
    params['pageIndex'] = str(i)
    response = requests.post(url=url1,params=params,headers=headers1)

    # 3.获取响应
    for store in response.json()['Table1']:
        result.append(store)
        print(store)
print('一共有' + str(len(result)) + '条数据。')

#4.持久化存储
DataFrame(result).to_excel('./广州所有kfc.xlsx',sheet_name='广州',index=False)    #rownum是天然的索引，故index=False表示不需要生成索引
print('保存到”广州所有kfc.xlsx“文件里了捏。')