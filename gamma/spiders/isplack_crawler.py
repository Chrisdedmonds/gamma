# -*- coding: utf-8 -*-
import scrapy


class IsplackCrawlerSpider(scrapy.Spider):
    name = 'isplack-crawler'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
