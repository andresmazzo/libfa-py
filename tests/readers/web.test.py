#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../../')

from libfa.services.readers.html.web import reader

pagename = sys.argv[1]
uri = sys.argv[2]

print('')
print('--- Read html web ---')
print('')

db = reader.get_page(pagename, uri)

print('content:')
print(db)


print('Finish! :tada:')