#!/usr/bin/python3

import sys
import os
import requests

def get(htmlWebpath):
  with urllib.request.urlopen(htmlWebpath) as response:
    htmldoc = response.read()
    soup = BeautifulSoup(htmldoc, 'html.parser')
    
    return get_data(soup)


def get_data(soup):
  data = {};
  data['categories'] = []

  dom_container = soup.find("div", class_="home-cat-container");

  for item in dom_container.find_all('div', class_="home-cat-container"):
      cat_obj = {}
      dom_title = item.find("div", class_="catrd-title")
      cat_obj['name'] = dom_title.find('a').string
      
      data['categories'].append(cat_obj)

  return data
