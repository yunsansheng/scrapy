# scrapy api
- scrapy

  ```python
  ['Field', 
   'FormRequest', 
   'Item', 
   'Request',
   'Selector',
   'Spider',
   '__all__','__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_txv', 'exceptions', 'http', 
   #'item',
   'link', 'selector', 'signals', 
   #'spiders', 
   'twisted_version', 'utils', 'version_info']
  ```

  

  - scrapy.Item 或 scrapy.item.Item

  - scrapy.Field() 或 scrapy.item.Field() ：加括号是实例化

  - scrapy.Spider ：基本的爬虫类

    - self.log :用于debug输出

  - genspider(默认basic) :用于生成spider
    `scrapy genspider [options] <name> <domain>` name 和 domain必填
    - basic

      ```
      scrapy genspider myname qsones.com
      ```
    - crawl 

      ```
      scrapy genspider -t crawl myname qsones.com
      ```
    - csvfeed
    - xmlfeed

  - parse

  - shell

  - ItemLoader **注意，scrapy没有loader，所以直接用 scrapy.loader会报错**

    ```python
    from scrapy.loader import ItemLoader
    或者
    import scrapy.loader
    #因为import scrapy 后并没有loader 所以用scrapy.loader就会报错
    ```

    - scrapy.loader.processors

      -  `from scrapy.loader.processors import MapCompose,Join`

        ```
        ['__call__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
        ```

        用法： 直接在add_xpath的时候传MapCompose， re 等。

        ```python
        l.add_xpath('title','//div/a/text()',MapCompose(fun1,fun2,fun3..))
        #e.g.
        l.add_xpath('title','//div/a/text()',MapCompose(float,lambda i:i*2),re='[0-9]') #==========这里的用法比较实用
        
        #也可以直接用
        #MapCompose(unicode.strip)([u' i am', u'  i like '])#注意会报错，python3中，用str代替unicode
        MapCompose(str.strip)([u' i am', u'  i like '])
        # str.float
        # str.title(首字母大写其余小写)
        MapCompose(float)([1,'2','3'])
        MapCompose(lambda rt :urlparse.urljoin(respnse.url,rt))(['url1','url2'])
        ```

        

```python
#item 代码示例
# -*- coding: utf-8 -*-
import scrapy
from properties.items import PropertiesItem

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['qsones.com']
    start_urls = ['http://qsones.com/']

    def parse(self, response):
        item =PropertiesItem()
        item['title']=response.xpath('//div/a/text()').extract()
        #...
        return item
    
$ scrapy crawl basic -o items.json
-o items.js
-o items.csv
-o items.xml
```



```python
#itemloader 代码示例

from scrapy.loader import ItemLoader
#...
#...
	def parse(self.response):
        l = ItemLoader(item = ProItem(),response=response)
        
        l.add_xpath('title','//div/a/text()')
        l.add_css()
        l.add_value()
        
        return l.load_item()
    # 方便之处在于 不用写extract（）
    # add_xpath更加简洁
    # itemloader提供了很多数据格式化和清洗的方式
```

