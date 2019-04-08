__author__ = 'Monty'
__date__ = '2018/8/28 上午10:19'

import pdfkit

options = {
    'page-size': 'A4',  # Letter
    'minimum-font-size': 25,  ###
    # 'image-dpi':1500, ###

    'margin-top': '0.1in',  # 0.75in
    'margin-right': '0.1in',
    'margin-bottom': '0.1in',
    'margin-left': '0.1in',
    'encoding': 'UTF-8',  # 支持中文
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'outline-depth': 10,
}

pdfkit.from_url('http://www.liujiangblog.com/course/django/2','./pdf/Django2.pdf',options=options)

