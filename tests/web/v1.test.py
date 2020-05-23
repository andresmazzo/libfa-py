#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path + '/../../')

import libfa

print('')
print('--- Web ---')
print('')

print(libfa.web.v1.locales())
print(libfa.web.v1.base_uri())
# print(libfa.web.html_v1.movie('ar', '1234'))

print('Finish! :tada:')