# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from symptom.items import SymptomItem, DiseaseItem

class SymptomPipeline(object):
    def process_item(self, item, spider):

        if isinstance(item,SymptomItem):
            print("url ---", item['url'])
            print("category ---",item['category'])
            print("symptoms ---", item['symptoms'])
        elif isinstance(item,DiseaseItem):
            print("url ---", item['url'])
            print("category ---",item['category'])
            print("disease_list ---", item['disease_list'])

        print('')
        return item
