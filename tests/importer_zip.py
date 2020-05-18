#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')

from libfa.services.importers.zipdata import main as fazip

zipFilepath = sys.argv[1]

print('')
print('--- Load zip file ---')
print('')

db = fazip.exec(zipFilepath)

print('data extracted from user exported zip:')
print(db)


print('Finish! :tada:')