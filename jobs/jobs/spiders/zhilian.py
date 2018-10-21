# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest





class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['qsones.com']


    def start_requests(self):
        return[
            FormRequest(
                "http://www.qsones.com",
                formdata={"user":"one","pass":"123"}
            )
        ]


    def parse(self, response):
        print(response.text)
