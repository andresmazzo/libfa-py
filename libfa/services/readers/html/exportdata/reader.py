#!/usr/bin/python3

import sys
import os

import pages.index as lindex
import pages.movie_ratings as lmovieratings
import pages.lists as llists
import pages.account_data as laccountdata
import pages.friend_groups as lfriendgroups

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../../../../utils')

import htmlr as htmlutil

def get_all(basePath):
  db = {}

  db['index'] = get_page(basePath, 'index')
  db['account_data'] = get_page(basePath, 'account-data')
  db['movie_ratings'] = get_page(basePath, 'movie-ratings')
  db['lists'] = get_page(basePath, 'lists')
  db['friend_groups'] = get_page(basePath, 'friend-groups')

  # TODO: Implement get_section
  # TODO: Load all dir content

  return db

def get_section(basePath, section_name):
  return {
        'movie-review': get_section_movie_review(basePath),
        'list': get_section_list(basePath),
        'friend-group': get_section_friend_group(basePath)
    }[section_name]


def get_section_list(basePath):
  db = {}
  db['lists'] = get_page(basePath, 'lists')
  # iterate lists

  return db

def get_section_movie_review(basePath):
  db = {}
  db['lists'] = get_page(basePath, 'lists')
  # iterate lists

  return db

def get_section_friend_group(basePath):
  db = {}
  db['lists'] = get_page(basePath, 'lists')
  # iterate lists

  return db


def get_page(basePath, page_name):
  return {
      'index': lindex.get(basePath + '/index.html'),
      'account-data': laccountdata.get(basePath + '/html/account-data.html'),
      'friend-groups': lfriendgroups.get(basePath + '/html/friend-groups.html'),
      'lists': llists.get(basePath + '/html/lists.html'),
      'movie-ratings': lmovieratings.get(basePath + '/html/movie-ratings.html'),
      # 'movie-reviews': lmoviereviews.get(basePath + '/html/movie-reviews.html'),
  }[page_name]
