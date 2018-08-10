# 爬取国税系统所有知识文章 http://xt.szgs.gov.cn/Question/
import requests
from bs4 import BeautifulSoup

base_url = 'https://h5.ele.me/'

headers = {
    'upgrade-insecure-requests': '1',
    'cookie':'ubt_ssid=0aeuyg7ar52p3kc8td2p8plksylzgmbb_2018-08-04; _utrace=d0ed7898a6c5ee5ba351f4bcd23d647e_2018-08-04; perf_ssid=zu550jmlcternhzgzu6e7oq2k1sdh7pl_2018-08-04; track_id=1533394687|69e8ae981b261554daff710e506d757540f401e99783f0cb76|7b24e046f2b0e2dde8dd5948f8479923; USERID=23759892; SID=hWuI8SDc6TVMSMWRAMCcZspVPXtgy4z9XG9w',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Mobile Safari/537.36'
}
question_result = requests.get(base_url)  # 请求页面内容

soup = BeautifulSoup(question_result.content, 'lxml')
print(soup)

# pages_soup = soup.find('div', attrs={'class': 'page'})  # 获取页码
# pages = pages_soup.find_all('a')  # 获取页码中的链接
# max_page = pages[-1].get('href').split('page=')[-1]  # 获取最大页码，作为下面循环爬取的最大值

# for page in range(2, int(max_page) + 1):
#     page_url = '%s?page=%s' % (url, page)  # 拼接单页的绝对地址
#     print(page_url)
#     page_question_result = requests.get(page_url)
#     page_soup = BeautifulSoup(page_question_result.content, 'lxml')
#     question_list = []  # 存储一页所有的详情
#     kj = page_soup.find('div', attrs={'class': 'kj'})
#     links = kj.find_all('a') # 获取一页中所有item的a标签
#     print(links)
#
#     for link in links:  # 循环抓取每页的详情
#         a = link.get('href') # 获取a标签中href的值
#         text = link.text  # 获取到详情的相对地址
#         detail = basr_url + a  # 拼接详情页面的绝对地址
#         print(detail)
#         detail_result = requests.get(detail) # 请求详情页
#         detail_soup = BeautifulSoup(detail_result.content, 'lxml')
#         articleContent = detail_soup.find('div', attrs={'class': 'articleContent'}) # 获取到详情页中class为articleContent的内容
#         # articleContent_text = articleContent.text # 获取articleContent中的纯文本，取出其他所有标签
#         question = { # 封装需要的内容
#             'title': link.text,
#             'url': basr_url + a,
#             'content': articleContent.prettify()
#         }
#         question_list.append(question) # 将封装后的详情内容添加到当前页面集合中去
#
#     for question in question_list: # 爬取到一页数据并且封装完成之后，将当前列表中的所有详情写入到文件中
#         with open('./doc/%s.txt' % question['title'].strip(), 'w') as fp:
#             fp.write(question['content'])
