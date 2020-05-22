#!/usr/bin/python3

import sys
import os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../..')

import htmlr as htmlutil

def get(htmlFilepath):
  html_content = open(htmlFilepath, 'r').read()
  htmlr = htmlutil.load(html_content)

  return get_data(htmlr)


def get_data(htmlr):
  data = {};
  data['data'] = []

  dom_list = htmlr.lib().find("table", class_="movie-ratings")

  for item in dom_list.find_all('tr'):
      tds = item.find_all('td')
      rating = {}
      rating['value'] = tds[0].find("div", class_="user-rating").string
      rating['movie_name'] = tds[1].string
      rating['created_at'] = tds[2].string
      
      data['data'].append(rating)
  
  return data