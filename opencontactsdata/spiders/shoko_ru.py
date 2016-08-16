# -*- coding: utf-8 -*-

import scrapy
import csv
import io
import time

class ShokoRUSpider(scrapy.Spider):
    name = 'shoko_ru'
    start_urls = ['http://shoko.ru/moskva/adresa_kofeen/']

    def parse(self, response):
        for town in response.css('select[name=towns] option').xpath('@value').extract():
            if town:
                yield scrapy.Request('http://shoko.ru/bitrix/templates/shoko/js/autogoogle/{0}/all.txt'.format(town), self.parse_town)

    def parse_town(self, response):
        ts = time.time()
        f = io.StringIO(response.text)
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            yield {
                'source': 'shoko.ru',
                'lat': row[0],
                'lon': row[1],
                'address': row[2],
                'phone': row[3],
                'opening_hours': row[4],
                'crawl_time': ts,
            }
