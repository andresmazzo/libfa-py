#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, path + '/')
import pages.index as lindex

sys.path.insert(0, path + '/../../../../utils')

import htmlr as htmlutil


def get_page(page_name, uripath):
  page_readers = {
      'index': lindex,
      # 'account-data': laccountdata,
      # 'friend-groups': lfriendgroups,
      # 'friend-group': lfriendgroup,
      # 'lists': llists,
      # 'list': llist,
      # 'movie-ratings': lmovieratings,
      # 'movie-reviews': lmoviereviews
  }  

  page_reader = page_readers[page_name]

  return page_reader.get(uripath)
