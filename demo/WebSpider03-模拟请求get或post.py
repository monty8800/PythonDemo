import urllib.request, parser
import json

# 3.模拟请求get或post
# 模拟get
# get_url = "http://gank.io/api/data/" + urllib.request.quote("福利") + "/1/1"
# get_resp = urllib.request.urlopen(get_url)
#
# json_res = json.loads(get_resp.read().decode('utf-8'))
# print(json_res)
#
# # 格式化json输出格式
# get_result_format = json.dumps(json_res, indent=2, sort_keys=True, ensure_ascii=False)
# print(get_result_format)


# 模拟post
post_url = 'http://mwu.me/index.php/action/login?_=bda051428ff09c1f114adf2632fdd3c6'
name = 'xxx'
password = 'xxx'
referer = 'http:mwu.me/admin'
values = {'name': name, 'password': password, 'referer': referer}
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/63.0.3239.84 Safari/537.36',
           'Referer': 'http:mwu.me/admin',
           'Connection': 'keep-alive'}
data = urllib.parse.urlencode(values).encode(encoding='utf-8')

req = urllib.request.Request(post_url, data, headers,)
# urlopen函数时添加timeout参数，单位是秒
resp = urllib.request.urlopen(req,timeout=30)

print('info -> ', resp.info())
print('code -> ', resp.getcode())

# result = json.loads(resp.read())    # Byte结果转Json
# print(json.dumps(result, sort_keys=True,indent=2, ensure_ascii=False)) # 格式化输出Json
