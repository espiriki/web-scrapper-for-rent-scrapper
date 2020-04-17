# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import JsonRequest
import ipdb
import json

class MyRentFasterSpider(scrapy.Spider):
    name = 'my_rent_faster'

    def start_requests(self):

        busca_url = "https://www.rentfaster.ca/api/map.json"

        dados = {"e": "zoom_changed", "l": "12,51.0687,-114.0899", "beds": ",bachelor", "baths": "1,1.5,2,2.5,1,1.5,2,2.5,3+", "type": "Apartment,Condo,Loft,Condo,Loft", "price_range_adv[from]": "0", "price_range_adv[to]": "1000", "furnishing": "Unfurnished", "area": "51.16417413931004,-113.96716211547852,50.97302850876522,-114.21263788452148"}

        yield JsonRequest(busca_url, data=dados,callback=self.parse)

    def parse(self, response):

        data = json.loads(response.text)

        imoveis = data["listings"]

        for imovel in imoveis:

            ipdb.set_trace()
