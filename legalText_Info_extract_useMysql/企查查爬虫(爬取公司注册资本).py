import random
import re
import time

import pandas as pd
from selenium import webdriver
import subprocess
import csv


def isElementExist(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False


csv_reader = csv.reader(open('all_company_csv.csv', encoding='GBK'))
date = []  # 创建列表准备接收csv各行数据
# print(type(date))
for one_line in csv_reader:
    date.append(one_line)

driver = webdriver.Chrome(executable_path="H:\selenium_chrome\dev\chromedriver.exe")
url = 'https://www.qcc.com'
driver.get(url)

# 点击关闭弹窗按钮
closeTagButton = driver.find_element_by_xpath('//*[@id="indexBonusModal"]/div/div/button')
closeTagButton.click()
# 扫码登陆
subprocess.call("pause", shell=True)

# 通过id信息来获取
input = driver.find_element_by_id('searchkey')
input.send_keys('test')  # 在输入框里输入搜索关键词
searchButton = driver.find_element_by_xpath('//*[@id="indexSearchForm"]/div/span/input')
searchButton.click()  # 点击搜索按钮

# textMoney = driver.find_element_by_xpath('//*[@id="search-result"]/tr[1]/td[3]/p[1]/span[1]').text
outCount = 0
timeflag = 0
flag = 0
i = 0
try:
    for line in date:
        i += 1
        if i > 2600:
            if flag == 0:
                flag = flag + 1
                continue
            else:
                # 通过id信息来获取
                input = driver.find_element_by_id('headerKey')
                input.clear()
                input.send_keys(line[0])  # 在输入框里输入搜索关键词
                searchButton = driver.find_element_by_xpath('/html/body/header/div/form/div/div/span/button')
                searchButton.click()  # 点击搜索按钮
                time.sleep(random.randint(0, 1))
                moneyXpath = '//*[@id="search-result"]/tr[1]/td[3]/p[1]/span[1]'
                if isElementExist(moneyXpath) and bool(
                        re.search('注册资本：', driver.find_element_by_xpath(moneyXpath).text)):
                    textMoney = driver.find_element_by_xpath(moneyXpath).text
                    textMoney = textMoney.split('注册资本：')[1]
                else:
                    textMoney = '-'
                if bool(re.search('美元', textMoney)):
                    textMoney = textMoney.split('万美元')[0]
                    # 美元换算成人民币
                    textMoney = float(textMoney) * 7
                elif bool(re.search('人民币', textMoney)):
                    textMoney = textMoney.split('万元人民币')[0]
                else:
                    pass
                line[1] = textMoney
                outCount = outCount + 1
                print('当前id：', outCount)
                print("企业注册资本为：",textMoney)
                timeflag = timeflag + 1
                if timeflag == 100:
                    time.sleep(5)
                    timeflag = 0
except:
    companyMoney = pd.DataFrame(data=date)
    print(companyMoney)
    companyMoney.to_csv('all_company_result_csvTestex.csv', encoding='gbk', index=False, header=False)

companyMoney = pd.DataFrame(data=date)
print(companyMoney)
companyMoney.to_csv('all_company_result_csvTEst.csv', encoding='gbk', index=False, header=False)
