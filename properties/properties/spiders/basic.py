# -*- coding: utf-8 -*-
import scrapy
from  scrapy import Request
from urllib import parse as urlparse

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://web/']

    def parse(self, response):
        next_selector  =response.xpath('//*[contains(@calss,"next")]//@href')
        for url in next_selector.extract():
            yield Request(urlparse.urljoin(response.url,url))

        item_selector =response.xpath('//*[@itemprop="url"]/@href')
        for url in item_selector.extract():
            yield Request(urlparse.urljoin(response.url,url),callback=self.parse_item)


