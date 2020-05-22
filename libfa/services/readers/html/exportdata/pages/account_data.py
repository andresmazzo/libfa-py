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

  dom_list = htmlr.lib().find("table", class_="account-data")
  trs = dom_list.find_all('tr')

  data['nickname'] = trs[0].find('td').string
  data['username'] = trs[1].find('td').string
  data['email'] = trs[2].find('td').string
  data['birth_year'] = trs[3].find('td').string
  data['city'] = trs[4].find('td').string
  data['country'] = trs[5].find('td').string
  data['registered_at'] = trs[6].find('td').string
  data['social_medias'] = trs[7].find('td').string

  return data