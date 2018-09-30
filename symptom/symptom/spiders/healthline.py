# -*- coding: utf-8 -*-
import os
import scrapy
import json
from symptom.items import SymptomItem, DiseaseItem
from itertools import combinations

class HealthlineSpider(scrapy.Spider):
    name = 'healthline'
    allowed_domains = ['www.healthline.com']
    base_url = "https://www.healthline.com/symptom/"

    opt_list = ["symptom", "disease", "disease_list"]
    # start_urls = ['https://www.healthline.com/symptom/']

    def start_requests(self):
        try:
            category = self.category
        except AttributeError:
            category = "dizziness"
            self.category = "dizziness"

        try:
            crawl_opt = self.opt
        except AttributeError:
            self.opt = "symptom"

        if not self.opt in self.opt_list:
            # self.log.warning
            self.opt = "symptom"

        try:
            self.max_combine = int(self.max_combine)
        except AttributeError:
            self.max_combine = 2

        # url = 'https://www.healthline.com/symptom/{}'.format(category)

        url = os.path.join(self.base_url, category)

        if self.opt == "symptom":
            request = scrapy.Request(url, callback=self.parse_symptom)
        elif self.opt == "disease":
            request = scrapy.Request(url, callback=self.parse_disease)
        elif self.opt == "disease_list":
            request = scrapy.Request(url, callback=self.parse_other_symptoms)

        request.meta['category'] = category

        yield request

    def parse_other_symptoms(self, response):
        # print(response.url)
        # print("category = ",response.meta['category'])

        other_symptoms = self.get_other_symptoms(response)

        # print(other_symptoms)

        combination_categorys = self.create_combination_categorys(self.category, other_symptoms, self.max_combine)

        # [print(u) for u in combination_categorys]

        for category in combination_categorys:
            url = 'https://www.healthline.com/symptom/{}'.format(category)
            # print("Request:",url)
            request = scrapy.Request('https://www.healthline.com/symptom/{}'.format(category), callback=self.parse_disease)
            request.meta['category'] = category
            yield request

    def get_other_symptoms(self, response):
        p_list = []

        lines = response.text.splitlines()
        for line in lines:
            line = line.strip()
            if line.startswith("__NEXT_DATA__"):
                data = line.split("=",maxsplit=1)[1].strip()
                # print(data)

                d = json.loads(data)

                p_list = [rs['cfn'] for rs in d['props']['relatedSymptoms']]

        return p_list


    def create_combination_categorys(self, symptom, other_symptoms, max_combine_number = 2):
        combined_categorys = []

        smart_other_symptoms = ['-'.join(s2.lower().split(' ')) for s2 in other_symptoms]

        combined_symptoms = combinations(smart_other_symptoms,max_combine_number - 1)

        for c in combined_symptoms:
            u = os.path.join(symptom, *c)
            combined_categorys.append(u)

        return combined_categorys

    def parse_symptom(self, response):
        symptom_item = SymptomItem()
        p = response.xpath("//article/h2[contains(text(), 'Symptoms')]/following-sibling::p[1]/text()")

        text_list = response.xpath("//article/h2[contains(text(), 'Symptoms')]/following-sibling::ul[1]/li")
        symptoms = [l.xpath("text()").extract_first() for l in text_list]
        symptom_item['url'] = response.url
        symptom_item['symptoms'] = symptoms
        symptom_item['category'] = self.category

        return symptom_item

    def parse_disease(self, response):
        disease_item = DiseaseItem()

        disease_item['url'] = response.url
        disease_item['category'] = response.meta['category']

        h_list = response.xpath('//h2[@class="h1 css-kjyn3a egb32mv1"]')

        disease_list = [h.xpath("text()").extract_first() for h in h_list]
        disease_item['disease_list'] = disease_list

        return disease_item

