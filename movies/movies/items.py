# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join


class MoviesItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(
        output_processor=Join()
    )
    date = scrapy.Field(
        output_processor=Join()
    )
    url = scrapy.Field(
        output_processor=Join()
    )
