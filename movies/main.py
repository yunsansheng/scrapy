#coding:utf-8

from scrapy import cmdline

cmdline.execute('scrapy crawl piaohua  -o test1.json'.split())
