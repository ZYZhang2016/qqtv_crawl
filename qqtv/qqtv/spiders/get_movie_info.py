# -*- coding: utf-8 -*-
import scrapy
import pymongo
from qqtv.items import QqtvItem


class GetMovieInfoSpider(scrapy.Spider):
    name = 'get_movie_info'
    allowed_domains = ['v.qq.com']
    start_urls = ['http://v.qq.com/']

    def parse(self, response):
        item = QqtvItem()
        movie_list = response.xpath("//*[id='figures_list']")
        print movie_list
'''
        def find_movie_data(page_html):
        def find_movie_name(page_html):
            return page_html.strong.string

        def find_movie_score(page_html):
            single_digit = page_html.find(class_ = 'score_l').string
            decimal = page_html.find(class_ = 'score_s').string
            return '评分： '+single_digit+decimal

        def find_movie_cast(page_html):
            figures = []
            cast_lst = page_html.find(class_ = 'figure_desc').find_all('a')
            for cast in cast_lst:
                figures.append(cast.string)
            return ','.join(figures)

        def find_movie_viewernum(page_html):
            return page_html.find(class_ = 'figure_count').find(class_='num').string
'''
