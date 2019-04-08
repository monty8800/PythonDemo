__author__ = 'Monty'
__date__ = '2018/8/28 上午11:32'

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.google.com/')

browser.get('http://172.16.0.24:8080/')
browser.find_element_by_id('username').send_keys('system')
browser.find_element_by_id('password').send_keys('111111')
# browser.find_element_by_id('workDate').send_keys('2015-01-01')
browser.find_element_by_xpath('/html/body/form/div[4]/button').click()
