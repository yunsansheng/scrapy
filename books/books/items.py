# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookname = scrapy.Field()
    bookauthor = scrapy.Field()
    unlimited = scrapy.Field()
    price = scrapy.Field()
    star = scrapy.Field()
    commentscount = scrapy.Field()

