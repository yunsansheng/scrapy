# -*- coding: utf-8 -*-
import scrapy


class DyttSpider(scrapy.Spider):
    name = 'dytt'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://dytt8.net/']

    def parse(self, response):
        pass
