#!/usr/bin/python3

import sys
import os

import pages.index as lindex
import pages.movie_ratings as lmovieratings
import pages.list as llist
import pages.lists as llists
import pages.account_data as laccountdata
import pages.friend_groups as lfriendgroups

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../../../../utils')

import htmlr as htmlutil

def get_all(basePath):
  db = {}

  db['pages'] = {}
  db['pages']['index'] = get_page('index', basePath + '/index.html')
  db['pages']['account-data'] = get_page('account-data', basePath + '/html/account-data.html')
  db['pages']['movie-ratings'] = get_page('movie-ratings', basePath + '/html/movie-ratings.html')
  db['pages']['lists'] = get_page('lists', basePath + '/html/lists.html')
  db['pages']['friend-groups'] = get_page('friend-groups', basePath + '/html/friend-groups.html')

  db['sections'] = {}

  db['sections']['lists'] = []
  for list_data in db['pages']['lists']['data']:
    list_page = get_page('list', basePath + '/html/' + list_data['url'])
    db['sections']['lists'].append(list_page)

  # db['sections']['friend-group'] = get_section(basePath, 'friend-group')
  # db['sections']['list'] = get_section(basePath, 'list')
  # db['sections']['movie-review'] = get_section(basePath, 'movie-review')

  # TODO: Support all features (im threads, ignore movies, etc)

  return db

# def get_section(basePath, section_name):
#   return {
#         'movie-review': get_section_movie_review(basePath),
#         'list': get_section_list(basePath),
#         'friend-group': get_section_friend_group(basePath)
#     }[section_name]


# def get_section_list(basePath):
#   db = {}
#   for item in dom_list.find_all('tr'):
#     db['t'] = get_page(basePath, 'lists')
#   # iterate lists

#   return db

# def get_section_movie_review(basePath):
#   db = {}
#   db['lists'] = get_page(basePath, 'lists')
#   # iterate lists

#   return db

# def get_section_friend_group(basePath):
#   db = {}
#   db['lists'] = get_page(basePath, 'lists')
#   # iterate lists

#   return db


def get_page(page_name, filepath):
  page_readers = {
      'index': lindex,
      'account-data': laccountdata,
      'friend-groups': lfriendgroups,
      'lists': llists,
      'list': llist,
      'movie-ratings': lmovieratings,
      # 'movie-reviews': lmoviereviews
  }  

  page_reader = page_readers[page_name]

  return page_reader.get(filepath)
