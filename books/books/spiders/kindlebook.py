# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from books.items import BooksItem
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urljoin



class KindlebookSpider(scrapy.Spider):
    name = 'kindlebook'
    allowed_domains = ['amazon.cn'] 
    start_urls = ["https://www.amazon.cn/b?node=1993922071&pf_rd_p=71651cda-c38c-439b-91ed-f267f431217e&pf_rd_s=merchandised-search-4&pf_rd_t=101&pf_rd_i=1993922071&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=8J6Q4GBN3Q8GGBF818WD&pf_rd_r=8J6Q4GBN3Q8GGBF818WD&pf_rd_p=71651cda-c38c-439b-91ed-f267f431217e"]

    def parse(self, response):
    	# div id="mainResults" > ul 所有li
    	#    a-fixed-left-grid-col a-col-right
    	#
        main = ''
        if response.xpath('//div[@id="mainResults"]/ul/li') !=[]:
            main = response.xpath('//div[@id="mainResults"]/ul/li')
        elif response.xpath('//div[@id="atfResults"]/ul/li') !=[]:
            main = response.xpath('//div[@id="atfResults"]/ul/li')



        for bookitem in main: #atfResults #mainResults
        	yield {
        	    'bookname':bookitem.xpath('.//div[@class="a-fixed-left-grid"]//h2/text()').extract_first(),
        	    'bookauthor':bookitem.xpath('.//div[@class="a-fixed-left-grid"]//div[@class="a-row a-spacing-small"]/div[@class="a-row a-spacing-none"]/span[2]/text()').extract_first(),
        	    'unlimited':bool(bookitem.xpath('.//div[@class="a-fixed-left-grid"]//span[@class="s-icon s-icon-kindle-unlimited"]')),
        	    'price':bookitem.xpath('.//div[@class="a-fixed-left-grid"]//span[@class="a-size-base a-color-price s-price a-text-bold"][last()]/text()')[-1].extract(),#取最后一个
        	    #'star':'',
                'source':'z.cn',
        	    'commentscount':''
        	}

        next_page = response.xpath('//div[@id="pagn"]//a[@class="pagnNext"]/@href').extract_first()
        #nextd = 'https://www.amazon.cn'+ next_page
        print(next_page)
        if next_page is not None:
        	yield response.follow(next_page, self.parse)

    # def parse(self, response):

    #     main = ''
    #     if response.xpath('//div[@id="mainResults"]/ul/li') !=[]:
    #         main = response.xpath('//div[@id="mainResults"]/ul/li')
    #     elif response.xpath('//div[@id="atfResults"]/ul/li') !=[]:
    #         main = response.xpath('//div[@id="atfResults"]/ul/li')

    #     for bookitem in main:
    #         yield self.parse_item(bookitem)

    #     next_page = response.xpath('//div[@id="pagn"]//a[@class="pagnNext"]/@href').extract_first()
    #     print(next_page)
    #     if next_page is not None:
    #         yield response.follow(next_page, self.parse)

    # def parse_item(self,selector):

    #     l = ItemLoader(item=BooksItem(), selector = selector)

    #     l.add_xpath('bookname','.//div[@class="a-fixed-left-grid"]//h2/text()')
    #     l.add_xpath('bookauthor','.//div[@class="a-fixed-left-grid"]//div[@class="a-row a-spacing-small"]/div[@class="a-row a-spacing-none"]/span[2]/text()')
    #     l.add_xpath('unlimited','.//div[@class="a-fixed-left-grid"]//span[@class="s-icon s-icon-kindle-unlimited"]',MapCompose(lambda i: bool(i)))
    #     l.add_xpath('price','.//div[@class="a-fixed-left-grid"]//span[@class="a-size-base a-color-price s-price a-text-bold"][last()]/text()',MapCompose(lambda i: i[-1]))
    #     l.add_value('source','z.cn')




    #    return l.load_item()    
