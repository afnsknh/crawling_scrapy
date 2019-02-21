# -*- coding: utf-8 -*-
import scrapy


class DataXxiSpider(scrapy.Spider):
    name = 'data_xxi'
    start_urls = ['https://indoxxi.bz/21cineplex/']

    def parse(self, response):
        pass

        
