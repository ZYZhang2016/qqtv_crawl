# -*- coding: utf-8 -*-
import scrapy
import pymongo
from qqtv.items import QqtvItem


class GetMovieInfoSpider(scrapy.Spider):
    name = 'get_movie_info'
    allowed_domains = ['v.qq.com']
    #start_urls = []
    #重写start_requests()方法，自定义爬取的网址
    def start_requests(self):
        base_url = 'http://v.qq.com/x/list/movie?cate=10001&offset={}'
        for i in range(0,4980,30):
            target_ulr = base_url.format(i)
            yield self.make_requests_from_url(target_ulr)


    def parse(self, response):
        item = QqtvItem()
        movie_list = response.xpath("//ul[@class='figures_list']")
        for i in range(1,31):
            movie_path = "//li[{}]".format(i)

            item['movie_name'] = str(movie_list.xpath("{}//strong[@class='figure_title']/a/text()".format(movie_path)).extract())
            item['movie_url'] = str(movie_list.xpath("{}//strong[@class='figure_title']/a/@href".format(movie_path)).extract())
            item['movie_viewer_num'] = str(movie_list.xpath('{}/div[3]/span/text()'.format(movie_path)).extract())


            #get score
            single_digit = movie_list.xpath("{}//em[@class='score_l']/text()".format(movie_path)).extract()
            decimal = movie_list.xpath("{}//em[@class='score_s']/text()".format(movie_path)).extract()
            item['movie_score'] = str(single_digit[0]+decimal[0])

            #get cast
            figures = []
            cast_lst = movie_list.xpath("{}//div[@class='figure_desc']//a/text()".format(movie_path)).extract()
            figures.append(cast_lst)
            item['movie_actors'] = figures

            yield item



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
