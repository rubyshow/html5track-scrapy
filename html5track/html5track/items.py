# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Html5TrackItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    content = Field()
    createtime = Field()
    sourceTitle = Field()
    sourceLink = Field()
    html5trackLink = Field()
    pass
