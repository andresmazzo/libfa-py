  #!/usr/bin/python3

import sys
import os
import importlib

from libfa.web.v1.pages import get_page


def movie(locale, id):
  data = get_page('movie-info', web_uri(locale, '/film' + id + '.html'))

  return data

def top_fa(locale):
  get_page('movie-info', web_uri(locale, '/topgen.html'))
  return

def best_top(locale):
  get_page('best-top', web_uri(locale, '/best_top.html'))
  
  return


def director(name):
  return

def search(param):
  return  

def web_uri(locale, path):
  return base_uri() + '/' + locale + path

def locales():
  return [
    'ar', # argentina
    'au', # australia
    'bo', # bolivia
    'ca', # canada
    'cl', # chile
    'co', # colombia
    'cr', # costa rica
    'ec', # ecuador
    'es', # spain
    'ie', # irland
    'mx', # mexico
    'pe', # peru
    'uk', # united kingdom
    'us', # united states
    'uy', # uruguay
    've', # venezuela
  ]

def base_uri():
  return 'https://www.filmaffinity.com'
