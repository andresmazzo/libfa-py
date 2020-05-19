#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, path + '/')
import pages.index as lindex
import pages.movie_info as lmovieinfo

sys.path.insert(0, path + '/../../../../utils')

import htmlr as htmlutil


def get_page(page_name, uripath):
  page_readers = {
      'index': lindex,
      'movie-info': lmovieinfo
  }  

  page_reader = page_readers[page_name]

  return page_reader.get(uripath)
