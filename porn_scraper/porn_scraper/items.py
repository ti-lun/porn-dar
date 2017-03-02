# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PornScraperItem(scrapy.Item):
    image_urls = scrapy.Field()
    title = scrapy.Field()
    images = scrapy.Field()
