import requests
import json
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
response = requests.get(url)
i = input("请输入要翻译的内容:")
data = {"i": i, "from": "zh-CHS", "to": "en", "doctype": "json"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"}
response = requests.post(url, data=data, headers=headers)

html = response.text
dict_str = json.loads(html)
print("翻译结果是:", dict_str["translateResult"][0][0]['tgt'])
