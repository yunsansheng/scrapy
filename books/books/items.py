# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join

class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookname = scrapy.Field(output_processor=Join())
    bookauthor = scrapy.Field(output_processor=Join())
    unlimited = scrapy.Field()
    price = scrapy.Field(output_processor=Join())
    star = scrapy.Field(output_processor=Join())
    commentscount = scrapy.Field(output_processor=Join())
    source = scrapy.Field(output_processor=Join())
    addtime = scrapy.Field(output_processor=Join())

