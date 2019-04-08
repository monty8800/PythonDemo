__author__ = 'Monty'
__date__ = '2018/12/21 4:51 PM'


import requests
url = 'https://play.google.com'

question_result = requests.get(url)
print(question_result.content)