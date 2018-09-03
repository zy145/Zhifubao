import json

import requests
from selenium import webdriver
import time
"""

const URL_TB_LOGIN = "https://member1.taobao.com/member/fresh/account_management.htm";
const URL_CHECK_IN = 'https://mbillexprod.alipay.com/enterprise/tradeListQuery.htm';

"""

url = 'https://auth.alipay.com/login/index.htm'

driver = webdriver.Chrome()

driver.get(url)

a = driver.find_element_by_link_text('商户服务')

a.click()

b = driver.find_element_by_link_text('对账中心')
b.click()

c = driver.find_element_by_link_text('卖出交易')
c.click()

data_list = driver.find_elements_by_xpath('//*[@id="root"]/div/div/div/div[4]/div[2]/div/div/div/div/div/div[1]/div/table/tbody/tr')

list = []

for data in data_list:
    temp = {}

    temp['create_time'] = data.find_element_by_xpath('./td/span/span/span[1]').text
    temp['order_name'] = data.find_element_by_xpath('./td[2]/div/div[1]').text
    temp['order_num'] = data.find_element_by_xpath('./td[2]/div/div[2]/span/span').text
    temp['pay_num'] = data.find_element_by_xpath('./td[3]/div/span/span').text
    temp['buyer_info_email'] = data.find_element_by_xpath('./td[4]/div/div[1]').text
    temp['buyer_info_name'] = data.find_element_by_xpath('./td[4]/div/div[2]').text
    temp['order_amount'] = data.find_element_by_xpath('./td[5]/div/span/span').text
    temp['trading_status'] = data.find_element_by_xpath('./td[8]/span/span').text

    print(temp)
    list.append(temp)


for data in list:
    json_data = json.dumps(data,ensure_ascii=False) + ',\n'




















