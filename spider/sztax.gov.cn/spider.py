# 爬取国税系统所有知识文章 http://xt.szgs.gov.cn/Question/
import requests
from bs4 import BeautifulSoup

basr_url = 'http://xt.szgs.gov.cn'
url = 'http://xt.szgs.gov.cn/Question/'

headers = {
    'Host': 'xt.szgs.gov.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
question_result = requests.get(url)  # 请求页面内容

soup = BeautifulSoup(question_result.content, 'lxml')

pages_soup = soup.find('div', attrs={'class': 'page'})  # 获取页码
pages = pages_soup.find_all('a')  # 获取页码中的链接
max_page = pages[-1].get('href').split('page=')[-1]  # 获取最大页码，作为下面循环爬取的最大值

for page in range(2, int(max_page) + 1):
    page_url = '%s?page=%s' % (url, page)  # 拼接单页的绝对地址
    print(page_url)
    page_question_result = requests.get(page_url)
    page_soup = BeautifulSoup(page_question_result.content, 'lxml')
    question_list = []  # 存储一页所有的详情
    kj = page_soup.find('div', attrs={'class': 'kj'})
    links = kj.find_all('a') # 获取一页中所有item的a标签
    print(links)

    for link in links:  # 循环抓取每页的详情
        a = link.get('href') # 获取a标签中href的值
        text = link.text  # 获取到详情的相对地址
        detail = basr_url + a  # 拼接详情页面的绝对地址
        print(detail)
        detail_result = requests.get(detail) # 请求详情页
        detail_soup = BeautifulSoup(detail_result.content, 'lxml')
        articleContent = detail_soup.find('div', attrs={'class': 'articleContent'}) # 获取到详情页中class为articleContent的内容
        # articleContent_text = articleContent.text # 获取articleContent中的纯文本，取出其他所有标签
        question = { # 封装需要的内容
            'title': link.text,
            'url': basr_url + a,
            'content': articleContent.prettify()
        }
        question_list.append(question) # 将封装后的详情内容添加到当前页面集合中去

    for question in question_list: # 爬取到一页数据并且封装完成之后，将当前列表中的所有详情写入到文件中
        with open('./doc/%s.txt' % question['title'].strip(), 'w') as fp:
            fp.write(question['content'])
