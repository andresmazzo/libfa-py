#!/usr/bin/python3

import sys
import os
import microdata
import urllib.request

def get(htmlWebpath):
  with urllib.request.urlopen(htmlWebpath) as response:
    html = response.read()
    
    return get_data(html)


def get_data(html):
  data = {};

  items = microdata.get_items(html)
  movie_item = items[0]
  data['microdata'] = movie_item

  return data
