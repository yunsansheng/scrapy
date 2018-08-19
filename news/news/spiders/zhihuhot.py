# -*- coding: utf-8 -*-
import scrapy


class ZhihuhotSpider(scrapy.Spider):
    name = 'zhihuhot'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def parse(self, response):
        pass
