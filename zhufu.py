import requests
from selenium import webdriver


class Zhifubao(object):
    def __init__(self):
        self.url = 'https://login.taobao.com/member/login.jhtml'
        self.driver = webdriver.Chrome()
        self.file = open('zhifu.json','w')

    def parse_data(self):


        a = self.driver.find_element_by_xpath('//*[@id="J_SiteNavLoginPanel"]/div/div[2]/p[1]/a[1]')
        a.click()

        b = self.driver.find_element_by_xpath('//*[@id="newAccountManagement"]/a')
        b.click()

        c = self.driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div[2]/p/a[1]')
        c.click()

    def run(self):
        self.driver.get(self.url)
        self.parse_data()




if __name__ == '__main__':
    zhifubao = Zhifubao()
    zhifubao.run()