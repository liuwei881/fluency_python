#coding=utf-8

import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):     # 1
        return SentenceIterator(self.words)     # 2


class SentenceIterator:
    def __init__(self, words):
        self.words = words      # 3
        self.index = 0      # 4

    def __next__(self):
        try:
            word = self.words[self.index]   # 5
        except IndexError:
            raise StopIteration()   # 6
        self.index += 1     # 7
        return word     # 8

    def __iter__(self):     # 9
        return self