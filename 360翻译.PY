import requests
import json
url = 'http://fanyi.so.com/index/search?'

query = input('请输入你要翻译的内容：')
query_string = {}
query_string['eng']='0'
query_string['validate']=''
query_string['ignore_trans']='0'
query_string['query']= query
headers = {'pro':'fanyi'}
response = requests.post(url=url,data=query_string,headers=headers)
response.encoding = 'utf-8'
dict_ret = json.loads(response.text)
print(dict_ret['data']['fanyi'])
