#!/usr/bin/env python3

import pytest
import os
import sys
print(os.getcwd())
print(sys.path)

from symptom.doctor import Transformer
from scrapy.http.response.html import HtmlResponse


class TestTransformer:
    def test_init(self):
        trans = Transformer()
        assert 1

    def test_process(self):
        pass

    def test_get_plain_text(self):
        trans = Transformer()

        with open('tests/data/dizziness.html', 'rb') as f:
            response = HtmlResponse(url='https://www.healthline.com/symptom/dizziness', body=f.read())

            text = trans.get_plain_text(response)

            print(text)

    def test_get_words_list(self):
        pass
