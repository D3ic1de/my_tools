#!/user/bin/env python3

import requests

PROXY_POOL_URL = 'http://127.0.0.1:5555/random'
 
def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
    
def domain_scan(domain_name, sub_names):
    proxy = get_proxy()
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy,
    }
    for sub in sub_names:
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
        }
        url = f"https://{sub}.{domain_name}"
        try:
            requests.head = headers
            requests.get(url, proxies=proxies)
            print(f"[*]{url}")
        except requests.ConnectionError:
            # print("error")
            pass

if __name__ == '__main__':
    dom_name = input("enter the domain name:")

    with open(".\subdomain.txt") as file:
        sub_name = file.read()
        sub_dom = sub_name.splitlines()
        # print("文件中存在的子域名数量：{}".format(len(sub_dom)))
        # print("文件中子域名列表")
        # print(sub_dom)
    domain_scan(dom_name, sub_dom)