#!/usr/bin/python3

import sys
import os
from zipfile import ZipFile
from bs4 import BeautifulSoup

from libfa.importer.exportdata.pages import (page_account_data, page_friend_group, page_friend_groups, page_index, page_list, page_lists, page_movie_ratings)

def exec(inputZipFilepath):
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

def get_page(name, filepath):
  pages_dict = {
      'index': page_index,
      'account-data': page_account_data,
      'movie-ratings': page_movie_ratings,
      'list': page_list,
      'lists': page_lists,
      'friend-group': page_friend_group,
      'friend-groups': page_friend_groups
  }  

  page_reader = pages_dict[name]

  return page_reader.get_data(load_html(filepath))


def load_html(htmlFilepath):
  htmldoc = open(htmlFilepath, 'r').read()
  soup = BeautifulSoup(htmldoc, 'html.parser')

  return soup