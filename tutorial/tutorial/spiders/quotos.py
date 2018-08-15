import scrapy
from scrapy.loader import ItemLoader
from tutorial.items import TutorialItem
import json
from . import Wechat


#wechat =Wechat.Wechat()
#wechat.senddata('testtest','wangchao')

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page

        l = ItemLoader(item= TutorialItem(),response =response)

        l.add_value('title',filename)
        wehcat =Wechat.Wechat()
        wechat.senddata("testin","wangchao")
        return l.load_item()


wechat =Wechat.Wechat()
wechat.senddata('testtest','wangchao')