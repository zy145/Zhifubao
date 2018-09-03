# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhifubaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    create_time = scrapy.Field()
    order_name = scrapy.Field()
    order_num = scrapy.Field()
    pay_num = scrapy.Field()
    buyer_info = scrapy.Field()
    order_amount = scrapy.Field()
    trading_status = scrapy.Field()


