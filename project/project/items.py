# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    data = scrapy.Field()
    extence= scrapy.Field()
    content= scrapy.Field()
    link= scrapy.Field()
    pass
