from selenium import webdriver
import time
from datetime import timedelta, date

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import os

import json
import random
# import cehsi
import openpyxl
import requests
import time
from urllib.parse import unquote, quote
import re

# Workbook()方法 不用参数,会新建一个xlsx文件.
# wb = openpyxl.Workbook()
# # save()方法 一个参数,保存路径,会覆盖.
# wb.save('a.xlsx')

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chromedriver = "/usr/bin/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
#
#
# d = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
# d = webdriver.Firefox()
# d.get('https://www.baidu.com/baidu?tn=monline_7_dg&ie=utf-8&wd=ip')
#
# t = d.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr/td/span')
# print(t)
import requests
res = requests.get('http://myip.ipip.net', timeout=5).text
print(res)