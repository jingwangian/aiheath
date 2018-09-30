#!/usr/bin/env python3
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from .trainer import train_data


class NBSymptomIdentifier:
    """Symptom Identifier by using NaiveBayesClassifier"""

    def __init__(self):
        self.train()

    def __call__(self, words, method='naivebay'):
        """According to the words return a symptom or None

        method: 'naivebay' or 'mapping',default naviebay
        """
        symptom = self.nb_cl.classify(words)

        return symptom

    def train(self):
        """
        """
        self.nb_cl = NaiveBayesClassifier(train_data)
