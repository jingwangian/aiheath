# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['www.healthline.com']
    start_urls = ['https://www.healthline.com/symptom/dizziness']

    def parse(self, response):
        print(type(response))
        h2_list = response.xpath("//h2")

        for h in h2_list:
            t = h.xpath("text()").extract_first()
            # print(t, type(t))
            if t.lower().startswith('symptoms'):
                print(h)
                print(dir(h))
