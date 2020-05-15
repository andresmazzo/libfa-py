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
  data['exported_at'] = htmlr.lib().find("div", class_="download-ts").string;

  dom_userprofile = htmlr.lib().find("div", class_="profile-link")
  data['username'] = dom_userprofile.find("strong").string
  data['username_profile_url'] = dom_userprofile.find("a").string
  
  return data
