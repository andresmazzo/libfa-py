#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/..')

from libfa import fa

print('')
print('--- FA Class ---')
print('')

fa = fa.FA()

print('db:')
print(fa.db)


print('Finish! :tada:')