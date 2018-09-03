# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import time

from retrying import retry
from selenium import webdriver

from scrapy.http import HtmlResponse

class SeleniumMiddleware(object):
    def __init__(self):
        # 构建有界面的Chrome
        self.driver = webdriver.Chrome()

    @retry(stop_max_attempt_number=20, wait_fixed=2000)
    def retry_load_page(self, request, spider):
        try:
            # 如果这里出现异常则交给try捕获，那么retry则不会工作，所以在except需要主动raise 一个异常

            if "account_management.htm" in request.url:

                self.driver.find_element_by_xpath('//*[@id="main-content"]/div/div[2]/div/div[2]/h3/span')
            else:
                self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[4]/div[2]/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div/span/span')

        except:
            spider.logger.info("Retry <{}> page ({} times)".format(request.url, self.count))
            self.count += 1
            # 手动抛出异常交给retry捕获，如果retry重试20次后，则该异常交到上一级方法的try捕获
            raise Exception("<{}> not login".format(request.url))



    def process_request(self, request, spider):
        #if "php" in reqeust.url:
        if "account_management.htm" in request.url:
            self.count = 1
            #driver = webdriver.Chrome()
            self.driver.get(request.url)

            try:
                #time.sleep(5)
                self.retry_load_page(request, spider)
                html = self.driver.page_source
                # 返回自定义的响应对象给引擎，引擎判断是一个response对象，交给spider解析处理。则request不再交给下载器。
                return HtmlResponse(url=self.driver.current_url, body=html.encode("utf-8"), encoding="utf-8", request=request)
            except Exception as e:
                return None

        elif 'tradeListQuery.htm' in request.url:

            self.count = 1
            #driver = webdriver.Chrome()
            self.driver.get(request.url)

            try:
                #time.sleep(5)
                self.retry_load_page(request, spider)
                html = self.driver.page_source
                # 返回自定义的响应对象给引擎，引擎判断是一个response对象，交给spider解析处理。则request不再交给下载器。
                return HtmlResponse(url=self.driver.current_url, body=html.encode("utf-8"), encoding="utf-8", request=request)
            except Exception as e:
                return None
        else:
            raise Exception("<{}> not data fount".format(request.url))

    # def __del__(self):
    #     self.driver.quit()
