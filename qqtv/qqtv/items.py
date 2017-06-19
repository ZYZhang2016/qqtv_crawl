# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QqtvItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    content = scrapy.Field()
    ctime = scrapy.Field()

    movie_url = scrapy.Field()
    movie_name = scrapy.Field()
    movie_actors = scrapy.Field()
    movie_score = scrapy.Field()
    movie_viewer_num = scrapy.Field()
