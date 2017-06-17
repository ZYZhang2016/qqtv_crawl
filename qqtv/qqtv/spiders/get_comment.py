# -*- coding: utf-8 -*-
import scrapy
#from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
import re
import json
from qqtv.items import QqtvItem

class GetCommentSpider(scrapy.Spider):
    name = 'get_comment'
    allowed_domains = ['v.qq.com']
    start_urls = ['http://v.qq.com/']

    start_urls = ['https://v.qq.com/x/cover/on07p481keuoysc.html',]
    comment_url = 'http://coral.qq.com/article/{}/comment?commentid=0&reqnum=20'
    sns_url = 'http://sns.video.qq.com/fcgi-bin/video_comment_id?otype=json&callback=jQuery&op=3&vid='

    def parse(self, response):
        vid = re.search('vid: "(.*?)",',response.body.decode('utf-8'),re.S)
        if vid is not None:
            vid = vid.group(1)
        else:
            print('Can not found vid')
        sns_url = self.sns_url + vid
        yield Request(sns_url, callback='parse_id')

    def parse_id(self,response):
        id = re.search('"comment_id":"(.*?)",',response.body.decode('utf-8'),re.S).group(1)
        commentUrl = self.comment_url.format(id)
        yield Request(commentUrl, callback='parse_comment')

    def parse_comment(self, response):
        jsDict = json.loads(response.body.decode('utf-8'))
        jsData = jsDict['data']
        comments = jsData['commentid']
        for each in comments:
            item = QqtvItem()
            item['content'] = each['content']
            item['name'] = each['userinfo']['nick']
            item['ctime'] = each['timeDifference']
            #print(item['name'])
            #print(item['ctime'])
            #print(item['content'])
            #print('-------------------')
            print('用户\"{0}\"在{1}时留下评论： {2}'.format(item['name'],item['ctime'].item['content']))
            yield item
