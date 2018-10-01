#!/usr/bin/env python3

import pytest
import os
import sys

from doctor.transformer import Transformer


class TestTransformer:
    def test_init(self):
        trans = Transformer()
        assert isinstance(trans, Transformer)

    def test_call(self):
        trans = Transformer()

        text = trans("I am a student and studying englishx")

        assert text == "i am a student and study english"
