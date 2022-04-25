from selenium import webdriver
import time
from datetime import timedelta, date

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from post import *
from ph1 import *

import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

d = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
# d = webdriver.Chrome()


# d = webdriver.Firefox()

d.implicitly_wait(5)
def rw():
    time.sleep(1)


def dl(phone):
    d.get('https://www.chaojijishi.com/h5/#/pages/login/login?from=user')
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[1]/uni-input/div/input').send_keys(
        phone)
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[2]/uni-input/div/input').send_keys(
        123456)
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[3]/uni-view[1]/uni-view').click()
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[5]/uni-view/uni-view').click()
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[5]/uni-view[4]').click()
    rw()
    d.get('https://www.chaojijishi.com/h5/#/pages/subpack1/set/user-id-card-data?type=1')


def jiance():
    try:
        WebDriverWait(d, 10).until(lambda d: d.find_element_by_xpath('/html/body/uni-app/uni-toast/div/p'))
        # 获取提示语文本
        time.sleep(0.6)
        tip_msg = d.find_element_by_xpath('/html/body/uni-app/uni-toast/div/p').text
        print(tip_msg)
        if tip_msg == "提交成功":
            return 1
        return 0
    except TimeoutError:
        d.refresh()
        return 1
        #
    # retries = 1
    # while retries <= 5:
    #     try:
    #         quote = \
    #         wait.until(EC.element_to_be_clickable((By.XPATH, '//h4[@class="quote-number ng-binding"]'))).text.split(
    #             "#")[1]
    #     except TimeoutException:
    #         driver.refresh()
    #         retries += 1


def dj():
    time.sleep(0.8)
    # 跳过广告
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[4]/uni-view/uni-image/img').click()

    # 进入主菜单

    time.sleep(0.6)
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[3]/uni-view').click()

    time.sleep(0.5)
    # 进入我的
    d.find_element_by_xpath('/html/body/uni-app/uni-tabbar/div[1]/div[5]').click()

    # 进入设置
    time.sleep(2)
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]/uni-view[3]/uni-view/uni-view[1]/uni-image').click()

    # 进入实名认证
    time.sleep(0.6)
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view/uni-text[1]').click()
    # 去认证
    time.sleep(0.6)
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[3]').click()
    time.sleep(0.4)


def sm(xm, sfz):
    # 输入姓名
    rw()
    box_name = d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[2]/uni-input/div/input')
    box_name.send_keys(xm)

    time.sleep(0.9)
    # 输入身份证
    box_id = d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[3]/uni-input/div/input')
    box_id.send_keys(sfz)
    time.sleep(1)

    # 提交
    time.sleep(0.6)
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[3]/uni-view').click()

    a = jiance()
    if a == 1:
        print('成功')
    else:
        print('失败')
        d.refresh()
    print(d.title)
    print(d.current_url)

    time.sleep(3)
    # d.close()
    return a


def zy():
    rw()
    d.get('https://www.chaojijishi.com/h5/#/pages/subpack1/set/pay-pwd?type=1')
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]/uni-view[2]/uni-view/uni-input/div/input').send_keys(
        123456)
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[2]/uni-view[2]/uni-view/uni-input/div/input').send_keys(
        123456)
    rw()
    d.find_element_by_xpath('/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]').click()


def zz():
    rw()
    d.get('https://www.chaojijishi.com/h5/#/pages/subpack1/pay-model/JDpay')
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[1]/uni-view[1]').click()
    rw()
    # 输入号码
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view/uni-view[2]/uni-view[2]/uni-input/div/input').send_keys(
        17000653464)
    rw()
    # 输入积分
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view/uni-view[3]/uni-view[2]/uni-input/div/input').send_keys(
        5)

    # 输入密码
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view/uni-view[4]/uni-view[2]/uni-input/div/input').send_keys(
        123456)
    # 确定
    rw()
    d.find_element_by_xpath(
        '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[2]/uni-view[2]/uni-view/uni-view/uni-view[5]/uni-view[2]').click()


def auto():
    p = writeexcle()
    while p is None:
        return 0
    dl(p)
    # dj()
    x = outid()
    a = sm(x[0], x[1])
    while a == 0:
        x = outid()
        a = sm(x[0], x[1])
    zy()
    zz()
    d.close()
    return 1


i = 0
while auto() == 1:
    i += 1
    print(i)
    d = webdriver.Chrome(chrome_options=chrome_options, executable_path=chromedriver)
    d.implicitly_wait(5)
