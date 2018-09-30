# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SymptomItem(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field()
    symptoms = scrapy.Field()
    url = scrapy.Field()

class DiseaseItem(scrapy.Item):
    # define the fields for your item here like:
    category = scrapy.Field()
    disease_list = scrapy.Field()
    url = scrapy.Field()
