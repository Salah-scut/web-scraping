import requests
import pandas as pd

url1 = 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=119&type=all'

headers1 = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}

response = requests.get(url1,headers=headers1)

# print(response.json())

results = []
for i in response.json()['data']['list']:
    results.append(i)
pd.DataFrame(results).to_excel('./bilibili.xlsx',encoding='utf-8')
print(results)