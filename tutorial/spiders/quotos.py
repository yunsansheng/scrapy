import scrapy
from scrapy.loader import ItemLoader
from tutorial.items import TutorialItem
import json
import urllib.request

class Wechat(object):

    def __init__(self):
        self._corpid ='wx812ae8d875711da7'
        self._corpsecret ='sayc0NWKZ8p-sFIasvL0oTJbQipW9habOR5nMXvbBiQBdxBeqtavrG3va58ts33J' 
        self._accesstoken = self.gettoken(self._corpid,self._corpsecret)


    def gettoken(self,corpid,corpsecret):
        gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
        try:
            token_file = urllib.request.urlopen(gettoken_url)
        except urllib.error.HTTPError as e:
            print (e.code)
            print (e.read().decode("utf8"))
            sys.exit()
        token_data = token_file.read().decode('utf-8')
        token_json = json.loads(token_data)
        token_json.keys()
        token = token_json['access_token']
        return token

    def senddata(self,content,user):
        #can set the user="@all" to all
        #not set  "toparty":"1"  will not use to send party else ,will combine use and party
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self._accesstoken
        send_values = {
            "touser":user,
            "msgtype":"text",  
            "agentid":"2", #applycation id
            "text":{
                "content":content
               },
            "safe":"0"
            }
        send_data = json.dumps(send_values, ensure_ascii=False).encode(encoding='UTF8')
        send_request = urllib.request.Request(send_url, send_data)
        #response = json.loads(urllib2.urlopen(send_request).read())
        response =urllib.request.urlopen(send_request)
        msg =response.read()
        print (str(msg))

wechat =Wechat()
wechat.senddata('testtest','wangchao')

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
        wehcat =Wechat()
        wechat.senddata("testin","wangchao")
        return l.load_item()