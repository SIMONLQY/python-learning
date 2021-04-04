# 1.API(Web应用编程接口)可以自动申请网站的特定信息而不是整个网页
# Web API是网站的一部分。用于与使用非常具体的URL请求特定信息的程序
# 交互。这种请求被称为API调用。请求的数据将以易于处理的格式（json或csv）返回。

# 2.使用API调用请求数据
import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)
# 将API响应存储在一个变量中
response_dict = r.json()
# 处理结果
print(response_dict.keys())
