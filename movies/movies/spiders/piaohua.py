# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from movies.items import MoviesItem
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urljoin



class PiaohuaSpider(scrapy.Spider):
    name = 'piaohua'
    allowed_domains = ['piaohua.com']
    start_urls = ['https://www.piaohua.com/html/dianying.html']

    def parse(self, response):
        selectors = response.xpath('//div[@id="iml1"]/ul/li')
        for selector in selectors:
            yield self.parse_item(selector)

    def parse_item(self,selector):

        l = ItemLoader(item=MoviesItem(), selector = selector)

        l.add_xpath('name','.//a//strong//text()')
        l.add_xpath('url','.//a[@class="img"]/@href',MapCompose(lambda i: "http://www.piaohua.com"+ i))
        l.add_xpath('date','./span/font/text()', re="\d{4}-\d{2}-\d{2}")

        return l.load_item()
