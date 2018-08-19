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
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    # def start_requests(self):
    #     urls= ['http://www.dytt8.net/html/gndy/dyzz/index.html']
    #     next_page = response.xpath('//div[@class="x"]//a/@href').extract_first()
    #     if next_page is not None:
    #         scrapy.Request(next_page,callback=self.parse_page,response=response)
    #



    def parse(self, response):

        selectors =response.xpath('//div[@class="co_content8"]/ul//table')
        for selector in selectors:
            yield self.parse_item(selector)

        next_page = response.xpath('//div[@class="x"]//a/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            #self.start_urls.append(next_page)
            yield scrapy.Request(next_page,callback=self.parse)

    def parse_item(self,selector):

        l = ItemLoader(item=MoviesItem(), selector = selector)

        l.add_xpath('name','.//a[@class="ulink"]/text()')
        l.add_xpath('url','.//a[@class="ulink"]/@href',MapCompose(lambda i: "http://www.dytt8.net"+ i))
        l.add_xpath('dt','.//font/text()', re="\d{4}-\d{2}-\d{2}")

        return l.load_item()

