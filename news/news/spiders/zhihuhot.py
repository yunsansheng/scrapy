# -*- coding: utf-8 -*-
import scrapy


class ZhihuhotSpider(scrapy.Spider):
    name = 'zhihuhot'
    allowed_domains = ['zhihu.com']

    header = {'authority': 'www.zhihu.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1',
              'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
              'cookie': '_zap=13e490f9-766f-47e1-88a9-3f83e9486752; d_c0="AMCl8Bsj9A2PTtmfujf-vFxO3gAJ0nsl0SU=|1532502065"; q_c1=945c62c030224d9aaeaa09bef0cecb30|1532502065000|1532502065000; l_cap_id="MDk3Nzc3OGY5MTAxNGFlZmFkYjk2NjY5MDQ1ZGI3MTk=|1533626685|fc49f8350859b4489fd19c44d26d3c3b617e3e6c"; r_cap_id="YWNlOGM1ZTRmMDhjNDA4N2JhZTAyY2JhOTliYWIzMzU=|1533626685|85a947484dcf3ed7d4cb8c1fff6844bcdd1d42c1"; cap_id="NzhmZDlmNWVmNzRlNGMwYjlmYjNjZjUyY2VmYmYwZjk=|1533626685|5ddb114a25cc32370c55a32618912c4e68e11ec0"; _xsrf=a3OAvD7h3UIjLKG3fu69wQSqDvVcl58W; capsion_ticket="2|1:0|10:1534143540|14:capsion_ticket|44:MGQ2NjU1NmM2ZDIxNGJmNDhiZmU3ZmUwODEyNTQxMTA=|3a82a76371842c58148b14038763a1f7ee1565362aaa9d293696c13d9f639468"; z_c0="2|1:0|10:1534143554|4:z_c0|92:Mi4xdG5vOUFBQUFBQUFBd0tYd0d5UDBEU1lBQUFCZ0FsVk5RbnBlWEFDOGtCaE9VNnFCMm9YZG8xQWpaNXFMS0ZKWGlR|f1bbe3252d01ced85e96ded2b8ef717389617caaf572e9904d5d785881f2ec87"; __utmc=51854390; __utmv=51854390.100-1|2=registration_date=20140306=1^3=entry_date=20140306=1; __utma=51854390.643862264.1534146296.1534146296.1534149133.2; __utmz=51854390.1534149133.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; tgw_l7_route=b3dca7eade474617fe4df56e6c4934a3'}

    def start_requests(self):
        urls=['https://www.zhihu.com/billboard']

        for url in urls:
            yield scrapy.Request(url =url,headers=self.header,callback=self.parse)


    def parse(self, response):
        print(response.status)
