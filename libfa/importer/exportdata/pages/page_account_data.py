#!/usr/bin/python3

import sys
import os

def get_data(soup):
  data = {};

  dom_list = soup.find("table", class_="account-data")
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