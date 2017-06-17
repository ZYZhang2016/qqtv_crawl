# -*- coding: utf-8 -*-

# Scrapy settings for qqtv project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'qqtv'

SPIDER_MODULES = ['qqtv.spiders']
NEWSPIDER_MODULE = 'qqtv.spiders'

ITEM_PIPELINES = ['qqtv.pipelines.qqtvspiderPipline']

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'
COOKIES_ENABLED = True

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'qqtv_movie'
MONGODB_DOCNAME = 'movie_info'
