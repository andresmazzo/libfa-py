#!/usr/bin/python3

import sys
import os

def get_data(soup):
  data = {};
  data['data'] = []

  dom_list = soup.find("table", class_="lists")

  for item in dom_list.find_all('tr'):
      listobj = {}
      listobj['number'] = item.find('th').string
      tds = item.find_all('td')
      listobj['name'] = tds[0].find("a").string
      listobj['url'] = tds[0].find("a")['href']
      listobj['total'] = tds[1].string
      
      data['data'].append(listobj)
  
  return data