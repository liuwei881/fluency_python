#coding=utf-8


# import builtins
from collections import *
#
# pylookup = collections.ChainMap(locals(), globals(), vars(builtins))
# print(pylookup)

import os
import argparse


class DeepChainMap(ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)
