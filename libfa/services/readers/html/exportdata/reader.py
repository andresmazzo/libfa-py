#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, path + '/')
import pages.index as lindex
import pages.movie_ratings as lmovieratings
import pages.list as llist
import pages.lists as llists
import pages.account_data as laccountdata
import pages.friend_group as lfriendgroup
import pages.friend_groups as lfriendgroups

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

def get_page(page_name, filepath):
  page_readers = {
      'index': lindex,
      'account-data': laccountdata,
      'friend-groups': lfriendgroups,
      'friend-group': lfriendgroup,
      'lists': llists,
      'list': llist,
      'movie-ratings': lmovieratings,
      # 'movie-reviews': lmoviereviews
  }  

  page_reader = page_readers[page_name]

  return page_reader.get(filepath)
