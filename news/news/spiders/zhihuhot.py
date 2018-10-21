# -*- coding: utf-8 -*-
import scrapy
from news.items import NewsItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose



class ZhihuhotSpider(scrapy.Spider):
    name = 'zhihuhot'
    allowed_domains = ['zhihu.com']

    limit= 20

    header = {'authority': 'www.zhihu.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1',
              'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'
              }
    def start_requests(self):
        urls=['https://www.zhihu.com/billboard']

        for url in urls:
            yield scrapy.Request(url =url,headers=self.header,callback=self.parse)

    def parse(self, response):

        selectors = response.xpath('//div[@class="Card"]//a[@class="HotList-item"]')
        for selector in selectors:
            yield self.parse_item(selector)

    def parse_item(self, selector):

        l = ItemLoader(item=NewsItem(), selector=selector)

        l.add_xpath('title', './/div[@class="HotList-itemTitle"]/text()')
        l.add_xpath('url', './/a[@class="ulink"]/@href', MapCompose(lambda i: "http://www.dytt8.net" + i))
        l.add_xpath('hots', './/div[@class="HotList-itemMetrics"]/text()')
        l.add_value('source', self.name)


        return l.load_item()





