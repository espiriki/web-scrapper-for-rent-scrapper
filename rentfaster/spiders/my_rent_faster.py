# -*- coding: utf-8 -*-
import scrapy


class MyRentFasterSpider(scrapy.Spider):
    name = 'my_rent_faster'
    allowed_domains = ['https://www.rentfaster.ca/']
    start_urls = ['http://https://www.rentfaster.ca//']

    def parse(self, response):
        pass
