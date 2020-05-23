#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path + '/../')

import libfa

print('')
print('--- libfa ---')
print('')

print(libfa.version)
print(libfa.author)

print(libfa.web)
print(libfa.importer)
print(libfa.exporter)

print('')
print('Finish! :tada:')