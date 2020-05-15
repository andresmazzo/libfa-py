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

  dom_list = htmlr.lib().find("table", class_="lists")

  for item in dom_list.find_all('tr'):
      listobj = {}
      listobj['number'] = item.find('th').string
      tds = item.find_all('td')
      listobj['name'] = tds[0].find("a").string
      listobj['total'] = tds[1].string
      # TODO: Read list directory here to insert movies in list ?
      
      data['data'].append(listobj)
  
  return data