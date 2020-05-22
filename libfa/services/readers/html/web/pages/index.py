#!/usr/bin/python3

import sys
import os
import requests
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../..')

import htmlr as htmlutil

def get(htmlWebpath):
  r = requests.get(htmlWebpath)
  if r.status_code == 200:
    htmlr = htmlutil.load(r.content)
    
    return get_data(htmlr)


def get_data(htmlr):
  data = {};
  data['categories'] = []

  dom_container = htmlr.lib().find("div", class_="home-cat-container");

  for item in dom_container.find_all('div', class_="home-cat-container"):
      cat_obj = {}
      dom_title = item.find("div", class_="catrd-title")
      cat_obj['name'] = dom_title.find('a').string
      
      data['categories'].append(cat_obj)

  return data
