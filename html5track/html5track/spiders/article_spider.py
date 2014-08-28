#html5track spider

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider
#from scrapy.spider import BaseSpider
from scrapy.http import Request

from html5track.settings import *
from html5track.items import Html5TrackItem

import sys

class articleSpider(CrawlSpider):
  name = 'article'
  start_urls = [
        'http://news.html5tricks.com/category/programmer'
      ]
  
  def parse(self,response):
    item = Html5TrackItem()
    listSel = HtmlXPathSelector(response) 
    links = listSel.select('//h1[@class="entry-title"]/a/@href').extract()
    for link in links:
       item['html5trackLink'] = link
       yield Request(link,meta={'item':item},callback=self.parseDetail)

  def parseDetail(self,response):
    item = response.meta['item']
    article = HtmlXPathSelector(response)
    item['title'] = article.xpath('//h1/text()').extract()[0]
    item['content'] = article.xpath('//div[@class="entry-content"]/text()').extract()[0]
    item['createtime'] = article.xpath('//time[@class="entry-date"]/@datetime').extract()[0]
    return item

