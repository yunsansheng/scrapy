#coding:utf-8
#import urllib.request
import json
import requests

class Wechat(object):

    def __init__(self):
        self._corpid ='wx812ae8d875711da7'
        self._corpsecret ='sayc0NWKZ8p-sFIasvL0oTJbQipW9habOR5nMXvbBiQBdxBeqtavrG3va58ts33J' 
        self._accesstoken = self.gettoken(self._corpid,self._corpsecret)


    def gettoken(self,corpid,corpsecret):
        gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
        try:
            token_file = requests.get(gettoken_url)

        except Exception as e:
            print (e)
            sys.exit()
        token_data = token_file.content.decode('utf-8')
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
        print(send_data)
        #send_request = urllib.request.Request(send_url, send_data)
        #response = json.loads(urllib2.urlopen(send_request).read())
        #response =urllib.request.urlopen(send_request)

        response = requests.post(send_url,send_data)
        msg =response.content
        print (str(msg))



if __name__=="__main__":
    wechat=Wechat()
    wechat.senddata("test12",'wangchao')


"""
消息说明
http://mobile.51cto.com/app-show-452153.htm
可发送文本、图片、语音、视频、文件、图文等消息类型

#text消息
{ 
   "touser": "UserID1|UserID2|UserID3", 
   "toparty": " PartyID1 | PartyID2 ", 
   "totag": " TagID1 | TagID2 ", 
   "msgtype": "text", 
   "agentid": "1", 
   "text": { 
       "content": "Holiday Request For Pony(http://xxxxx)" 
   }, 
   "safe":"0" 
} 
参数  必须  说明
touser  否   UserID列表（消息接收者，多个接收者用‘|’分隔）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
toparty 否   PartyID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
totag   否   TagID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
msgtype 是   消息类型，此时固定为：text
agentid 是   企业应用的id，整型。可在应用的设置页面查看
content 是   消息内容
safe    否   表示是否是保密消息，0表示否，1表示是，默认0

#image消息
{ 
   "touser": "UserID1|UserID2|UserID3", 
   "toparty": " PartyID1 | PartyID2 ", 
   "msgtype": "image", 
   "agentid": "1", 
   "image": { 
       "media_id": "MEDIA_ID" 
   }, 
   "safe":"0" 
} 
参数  必须  说明
touser  否   UserID列表（消息接收者，多个接收者用‘|’分隔）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
toparty 否   PartyID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
totag   否   TagID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
msgtype 是   消息类型，此时固定为：image
agentid 是   企业应用的id，整型。可在应用的设置页面查看
media_id    是   媒体资源文件ID
safe    否   表示是否是保密消息，0表示否，1表示是，默认0

#voice消息
{ 
   "touser": "UserID1|UserID2|UserID3", 
   "toparty": " PartyID1 | PartyID2 ", 
   "totag": " TagID1 | TagID2 ", 
   "msgtype": "voice", 
   "agentid": "1", 
   "voice": { 
       "media_id": "MEDIA_ID" 
   }, 
   "safe":"0" 
} 
参数  必须  说明
touser  否   UserID列表（消息接收者，多个接收者用‘|’分隔）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
toparty 否   PartyID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
totag   否   TagID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
msgtype 是   消息类型，此时固定为：voice
agentid 是   企业应用的id，整型。可在应用的设置页面查看
media_id    是   媒体资源文件ID
safe    否   表示是否是保密消息，0表示否，1表示是，默认0

#video消息
{ 
   "touser": "UserID1|UserID2|UserID3", 
   "toparty": " PartyID1 | PartyID2 ", 
   "totag": " TagID1 | TagID2 ", 
   "msgtype": "video", 
   "agentid": "1", 
   " video": { 
       "media_id": "MEDIA_ID", 
       "title": "Title", 
       "description": "Description" 
   }, 
   "safe":"0" 
} 
参数  必须  说明
touser  否   UserID列表（消息接收者，多个接收者用‘|’分隔）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
toparty 否   PartyID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
totag   否   TagID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
msgtype 是   消息类型，此时固定为：video
agentid 是   企业应用的id，整型。可在应用的设置页面查看
media_id    是   媒体资源文件ID
title   否   视频消息的标题
description 否   视频消息的描述
safe    否   表示是否是保密消息，0表示否，1表示是，默认0

#file消息
{ 
   "touser": "UserID1|UserID2|UserID3", 
   "toparty": " PartyID1 | PartyID2 ", 
   "totag": " TagID1 | TagID2 ", 
   "msgtype": "file", 
   "agentid": "1", 
   "file": { 
       "media_id": "MEDIA_ID" 
   }, 
   "safe":"0" 
} 
参数  必须  说明
touser  否   UserID列表（消息接收者，多个接收者用‘|’分隔）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
toparty 否   PartyID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
totag   否   TagID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
msgtype 是   消息类型，此时固定为：file
agentid 是   企业应用的id，整型。可在应用的设置页面查看
media_id    是   文件ID
safe    否   表示是否是保密消息，0表示否，1表示是，默认0

#news消息
{ 
   "touser": "UserID1|UserID2|UserID3", 
   "toparty": " PartyID1 | PartyID2 ", 
   "totag": " TagID1 | TagID2 ", 
   "msgtype": "news", 
   "agentid": "1", 
   "news": { 
       "articles":[ 
           { 
               "title": "Title", 
               "description": "Description", 
               "url": "URL", 
               "picurl": "PIC_URL", 
           }, 
           { 
               "title": "Title", 
               "description": "Description", 
               "url": "URL", 
               "picurl": "PIC_URL", 
           }     
       ] 
   } 
} 
参数  必须  说明
touser  否   UserID列表（消息接收者，多个接收者用‘|’分隔）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
toparty 否   PartyID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
totag   否   TagID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
msgtype 是   消息类型，此时固定为：news
agentid 是   企业应用的id，整型。可在应用的设置页面查看
title   否   标题
description 否   描述
url 否   点击后跳转的链接。企业可根据url里面带的code参数校验员工的真实身份。具体参考“9 微信页面跳转员工身份查询”
picurl  否   图文消息的图片链接，支持JPG、PNG格式，较好的效果为大图640*320，小图80*80。如不填，在客户端不显示图片


#mpnews消息
注：mpnews消息与news消息类似，不同的是图文消息内容存储在微信后台，并且支持保密选项。

{ 
   "touser": "UserID1|UserID2|UserID3", 
   "toparty": " PartyID1 | PartyID2 ", 
   "totag": " TagID1 | TagID2 ", 
   "msgtype": "mpnews", 
   "agentid": "1", 
   "mpnews": { 
       "articles":[ 
           { 
               "thumb_media_id": "id", 
               "author": "Author", 
               "content_source_url": "URL", 
               "content": "Content" 
               "digest": "Digest description", 
               "show_cover_pic": "0" 
           }, 
           {  
               "thumb_media_id": "id", 
               "author": "Author", 
               "content_source_url": "URL", 
               "content": "Content" 
               "digest": "Digest description", 
               "show_cover_pic": "0" 
           } 
       ] 
       "media_id": "id" 
   } 
   "safe":"0" 
} 
参数  必须  说明
touser  否   UserID列表（消息接收者，多个接收者用‘|’分隔）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
toparty 否   PartyID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
totag   否   TagID列表，多个接受者用‘|’分隔。当touser为@all时忽略本参数
msgtype 是   消息类型，此时固定为：mpnews
agentid 是   企业应用的id，整型。可在应用的设置页面查看
articles    是   图文消息，一个图文消息支持1到10个图文
thumb_media_id  是   图文消息缩略图的media_id, 可以在上传多媒体文件接口中获得。此处thumb_media_id即上传接口返回的media_id
title   是   图文消息的标题
author  否   图文消息的作者
content_source_url  否   图文消息点击“阅读原文”之后的页面链接
content 是   图文消息的内容，支持html标签
digest  否   图文消息的描述
show_cover_pic  否   是否显示封面，1为显示，0为不显示
safe    否   表示是否是保密消息，0表示否，1表示是，默认0



"""