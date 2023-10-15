# coding:utf-8
import requests
 
PROXY_POOL_URL = 'http://127.0.0.1:5555/random'
 
def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
 
while True:
    proxy = get_proxy()
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy,
    }
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
    try:
        response = requests.get('http://httpbin.org/get', proxies=proxies, timeout=10)
        print(response.text)
        res= requests.get('https://www.baidu.com', proxies=proxies, timeout=5000, headers=headers)
        res.encoding=res.apparent_encoding
        print(res.text)
        break
    except Exception as e:
        print(e)