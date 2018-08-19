#coding:utf-8

from scrapy import cmdline

cmdline.execute('scrapy crawl dytt -s CLOSESPIDER_PAGECOUNT=3  -o test.json'.split())

#cmdline.execute('scrapy crawl piaohua -o movie.json'.split())