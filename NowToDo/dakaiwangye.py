# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 15:33:45 2017

@author: YuanYe
"""

from selenium import webdriver
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
#driver = webdriver.firefox(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
driver = webdriver.Firefox(executable_path = '\Python27\geckodriver.exe')
# 用get打开百度页面
driver.get("http://www.17huo.com/search.html?sq=2&keyword=%E5%A4%A7%E8%A1%A3")
# 查找页面的“设置”选项，并进行点击
driver.find_elements_by_link_text('设置')[0].click()
# 打开设置后找到“搜索设置”选项，设置为每页显示50条
driver.find_elements_by_link_text('搜索设置')[0].click()
sleep(2)
m = driver.find_element_by_id('nr')
sleep(2)
m.find_element_by_xpath('//*[@id="nr"]/option[3]').click()
sleep(2)
# 处理弹出的警告页面
driver.find_element_by_class_name("prefpanelgo").click()
sleep(2)
driver.switch_to_alert().accept()
sleep(2)
# 找到百度的输入框，并输入“selenium”
driver.find_element_by_id('kw').send_keys('selenium')
sleep(2)
# 点击搜索按钮
driver.find_element_by_id('su').click()
sleep(2)
# 在打开的页面中找到“Selenium - 开源中国社区”，并打开这个页面
driver.find_elements_by_link_text('Selenium - 开源中国社区')[0].click()