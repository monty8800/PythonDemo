import urllib.request


ip_list_url = 'http://api.xicidaili.com/free2016.txt'

resp = urllib.request.urlopen(ip_list_url, timeout=3)
html = resp.read()
print(html)

# 使用ip代理
ip_query_url = 'http://www.xicidaili.com/nn/1'
# 1.创建代理处理器，ProxyHandler参数是一个字典{类型:代理ip:端口}
proxy_support = urllib.request.ProxyHandler({'http': '183.159.91.167:18118'})
# 2.定制，创建一个opener
opener = urllib.request.build_opener(proxy_support)
# 3.安装opener
urllib.request.install_opener(opener)

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (X11; Linux x86_64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.84 Safari/537.36',
    'Host': 'www.xicidaili.com'
}
MAX_NUM = 10  # 有时网络堵塞，会报URLError错误，所以加一个循环
request = urllib.request.Request(ip_query_url, headers=headers)
for i in range(MAX_NUM):
    try:
        response = urllib.request.urlopen(request, timeout=20)
        html = response.read()
        print(html.decode('utf-8'))
        break
    except:
        if i < MAX_NUM - 1:
            continue
        else:
            print("urllib.error.URLError: <urlopen error timed out>")
