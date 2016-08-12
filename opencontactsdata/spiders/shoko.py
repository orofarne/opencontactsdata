# -*- coding: utf-8 -*-

import scrapy
import csv
import io

class ShokoSpider(scrapy.Spider):
    name = 'shokospider'
    start_urls = ['http://shoko.ru/moskva/adresa_kofeen/']

    def parse(self, response):
        for town in response.css('select[name=towns] option').xpath('@value').extract():
            if town:
                yield scrapy.Request('http://shoko.ru/bitrix/templates/shoko/js/autogoogle/{0}/all.txt'.format(town), self.parse_town)

    def parse_town(self, response):
        f = io.StringIO(response.text)
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            yield {'lat': row[0], 'lon': row[1], 'address': row[2], 'phone': row[3], 'opening_hours': row[4]}
