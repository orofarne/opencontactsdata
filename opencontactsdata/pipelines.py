# -*- coding: utf-8 -*-

import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class OpencontactsdataPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWriterPipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False).encode('utf8') + "\n".encode('utf8')
        self.file.write(line)
        return item
