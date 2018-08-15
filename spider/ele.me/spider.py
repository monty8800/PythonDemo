# 爬取国税系统所有知识文章 http://xt.szgs.gov.cn/Question/
import requests
import json
import csv
import time
import codecs
import os
from bs4 import BeautifulSoup

base_url = "https://h5.ele.me"
# 搜索关键字‘红包’，按销量排名
path = '/restapi/shopping/v2/restaurants/search?offset={}&limit=15&keyword=%E7%BA%A2%E5%8C%85&latitude={}&longitude={}&search_item_type=3&is_rewrite=1&extras[]=activities&extras[]=coupon&terminal=h5&order_by=6'
headers = {
    'cookie': 'ubt_ssid=p8ux178znue5oupczjv9mk3ndgoxa7na_2018-08-03; _utrace=df32858c1487abc2271aaee84371fffa_2018-08-03; perf_ssid=hy0bqvheka8gl00ccfl7z7s67x6jbku8_2018-08-03; track_id=1533293647|a624ee9e9e171933ea2a5e3b75c9429a167a23789b31ff8c8c|bd7a821e180c6efd15378dfdbfe6199f; USERID=23759892; SID=Kqzj5UsVbp4BNDyQyfMY7uWY1xnqf8b3Gfjg',
    'referer': 'https://h5.ele.me/search/',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Mobile Safari/537.36',
    'x-shard': 'loc=106.563674,29.555986',
    'x-accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
}


# page_size:要爬取的页数,latitude:维度，longitude:经度
def spider(page_size, latitude, longitude):
    restaurant_list = []
    for page in range(page_size):
        new_path = str(path).format(page * 15, latitude, longitude)
        # print(base_url + new_path)
        print('第{}页:'.format(page + 1))
        question_result = requests.get(base_url + new_path, headers=headers)  # 请求页面内容
        result_json_str = question_result.content

        result_json = json.loads(result_json_str)
        # print(str(result_json))
        insides = result_json['inside']['0']['restaurant_with_foods']

        for inside in insides:
            restaurant = inside['restaurant']
            re = {
                'name': restaurant['name'],
                'address': restaurant['address'],
                'phone': restaurant['phone'],
                'recent_order_num': restaurant['recent_order_num'],
                'promotion_info': restaurant['promotion_info']
            }
            print(restaurant['phone'])
            restaurant_list.append(re)
        # print(json.dumps(restaurant_list).encode('latin-1').decode('unicode_escape'))
        save2csv(restaurant_list)
        time.sleep(3)


def save2csv(restaurant_list):
    headers = ['name', 'address', 'phone', 'recent_order_num', 'promotion_info']
    with open('ele.csv', 'w', newline='', encoding='utf_8_sig') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(restaurant_list)


if __name__ == '__main__':
    spider(2, 32.142969, 118.884871)
# def unicode2utf8(text):
#     if type(text) is bytes:
#         return text.decode('unicode_escape')
#     elif type(text) is str:
#         return text.encode('latin-1').decode('unicode_escape')
#     else:
#         return text
