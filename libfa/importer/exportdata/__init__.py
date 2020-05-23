#!/usr/bin/python3

import sys
import os
from zipfile import ZipFile
from bs4 import BeautifulSoup


def support():
  return ['index', 'account-data', 'movie-ratings', 'lists', 'friend-groups']

def run(inputZipFilepath):
  outputDir = 'temp'
  with ZipFile(inputZipFilepath, 'r') as zipObj:
    zipObj.extractall(outputDir)

  data = get_all(outputDir)
  # TODO: Delete temp dir

  return data


def get_all(basePath):
  data = {}

  data['pages'] = {}
  data['pages']['index'] = get_page('index', basePath + '/index.html')
  data['pages']['account-data'] = get_page('account-data', basePath + '/html/account-data.html')
  data['pages']['movie-ratings'] = get_page('movie-ratings', basePath + '/html/movie-ratings.html')
  data['pages']['lists'] = get_page('lists', basePath + '/html/lists.html')
  data['pages']['friend-groups'] = get_page('friend-groups', basePath + '/html/friend-groups.html')

  data['sections'] = {}

  data['sections']['list'] = []
  for list_data in data['pages']['lists']['data']:
    page_data = get_page('list', basePath + '/html/' + list_data['url'])
    data['sections']['list'].append(page_data)

  data['sections']['friend-group'] = []
  for friend_group_data in data['pages']['friend-groups']['data']:
    page_data = get_page('friend-group', basePath + '/html/' + friend_group_data['filepath'])
    data['sections']['friend-group'].append(page_data)

  # TODO: Support all features (im threads, ignore movies, etc)

  return data


def load_html(htmlFilepath):
  htmldoc = open(htmlFilepath, 'r').read()
  soup = BeautifulSoup(htmldoc, 'html.parser')

  return soup