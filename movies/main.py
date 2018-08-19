#coding:utf-8

from scrapy import cmdline

cmdline.execute('scrapy crawl dytt -s CLOSESPIDER_PAGECOUNT=10  -o test.json'.split())
