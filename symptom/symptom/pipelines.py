# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pprint import pprint
from symptom.items import SymptomItem, DiseaseItem


class SymptomPipeline(object):
    def process_item(self, item, spider):

        if isinstance(item, SymptomItem):
            pprint(dict(item))
            # pprint(item['url'])
            # pprint(item['category'])
            # pprint(item['symptoms'])
        elif isinstance(item, DiseaseItem):
            pprint(dict(item))
            # pprint("url ---", item['url'])
            # pprint("category ---", item['category'])
            # pprint("disease_list ---", item['disease_list'])

        print('')
        return item
