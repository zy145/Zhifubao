# -*- coding: utf-8 -*-
import scrapy
import time


class ZhifubaoSpider(scrapy.Spider):
    name = 'zhifubao'
    allowed_domains = ['alipay.com']
    base_url = 'https://member1.taobao.com/member/fresh/account_management.htm'
    start_urls = [base_url]


    def parse(self, response):
        if response.body:
            url = 'https://mbillexprod.alipay.com/enterprise/tradeListQuery.htm'
            while True:
                yield scrapy.Request(url, callback=self.parse_item, dont_filter=True)
                time.sleep(1)

    def start_requests(self):
        while True:
            # 需要发起这个请求，才能获取到列表页数据，并且返回的是一个js语句
            url = "https://member1.taobao.com/member/fresh/account_management.htm"
            yield scrapy.Request(url, callback=self.parse)
            time.sleep(10)


    def parse_item(self, response):
        print(response.xpath('//*[@id="root"]/div/div/div/div[4]/div[2]/div/div/div/div/div/div[1]/div/table/tbody/tr/td[3]/div/span/span/text()').extract_first())





