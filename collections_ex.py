#coding=utf-8


# import builtins
import collections
#
# pylookup = collections.ChainMap(locals(), globals(), vars(builtins))
# print(pylookup)

import os
import argparse


defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}

combined = collections.ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])
