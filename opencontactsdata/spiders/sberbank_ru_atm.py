# -*- coding: utf-8 -*-

import scrapy
from io import BytesIO
from openpyxl import Workbook, load_workbook
import time

class SberbankRUSpider(scrapy.Spider):
    name = 'sberbank_ru_atm'
    start_urls = ['http://www.sberbank.ru/common/img/uploaded/cards/atm.xlsx']

    def parse(self, response):
        ts = time.time()
        wb = load_workbook(filename=BytesIO(response.body))
        sheet = wb.active
        for row in sheet.rows:
            if row[0].value.isdigit():
                yield {
                    'source': 'sberbank.ru',
                    'external_id': row[0].value,
                    'region': row[1].value,
                    'place': row[2].value,
                    'address': row[3].value,
                    'comment': 'Расположен в {0}, тип: {1}'.format(row[4].value, row[11].value),
                    'phone': row[8].value,
                    'opening_hours': row[9].value,
                    'lat': row[12].value,
                    'lon': row[13].value,
                    'crawl_time': ts,
                }
