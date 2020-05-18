#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')

from libfa.services.readers.html.exportdata import reader

htmlBasepath = sys.argv[1]

print('')
print('--- Read html exportdata ---')
print('')

db = reader.get_all(htmlBasepath)

print('content:')
print(db)


print('Finish! :tada:')