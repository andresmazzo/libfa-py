#!/usr/bin/python3

import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../../../../../utils')

import htmlr as htmlutil

def get(htmlFilepath):
  html_content = open(htmlFilepath, 'r').read()
  htmlr = htmlutil.load(html_content)

  return get_data(htmlr)


def get_data(htmlr):
  data = {};
  data['data'] = []

  data['name'] = htmlr.lib().title.string
  dom_list = htmlr.lib().find("table", class_="ml")

  for item in dom_list.find_all('tr'):
      listobj = {}
      listobj['friend_name'] = item.find("td").string
      
      data['data'].append(listobj)
  
  return data