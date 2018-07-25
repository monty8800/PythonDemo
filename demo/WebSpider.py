import urllib.request, parser
import json

# 1.爬取网页
html_url = 'http://mwu.me'
html_resq = urllib.request.urlopen(html_url)

# 读取全部，读取一行可用readline()，多行返回列表的可用readlines()
html = html_resq.read()
html = html.decode('utf-8')
print(html)

html_re_info = html_resq.info() # 获取头信息
html_re_code = html_resq.getcode() # 状态码
html_re_url = html_resq.geturl() # 请求的url

print(html_re_info)
print(html_re_code)
print(html_re_url)

# 2.爬取二进制文件
img_url = 'http://mwu.me/usr/uploads/2018/07/1928042616.png'
img_resp = urllib.request.urlopen(img_url)
img = img_resp.read()
with open('user.png','wb') as f:
    f.write(img)


urllib.request.urlretrieve(img_url,'./files/u.png')

# 也可以直接调用urlretrieve下载，比如下载音频
music_url = "http://mwu.me/usr/uploads/2018/07/3708374225.pdf"
urllib.request.urlretrieve(music_url, "./files/文档.pdf")


# 3.模拟请求get或post
get_url = "http://gank.io/api/data/" + urllib.request.quote("福利") + "/1/1"
get_resp = urllib.request.urlopen(get_url)

print(get_resp)






