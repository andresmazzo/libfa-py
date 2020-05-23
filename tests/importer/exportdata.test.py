#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../../')

import libfa

zipFilepath = sys.argv[1]

print('')
print('--- Load zip file ---')
print('')

db = libfa.importer.run('exportdata', zipFilepath)

print('data extracted from user exported zip:')
print(db)
print('')
print('Finish! :tada:')