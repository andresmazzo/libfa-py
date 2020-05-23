#!/usr/bin/python3

import sys


class DB:
  def __init__(self, name):
    self.name = name
    self.init_db();

  def init_db(self):
    self.db = {}
    self.db['user'] = {} # account, friends, lists, ratings, etc
    self.db['medias'] = {} # movies and tv shows

  def get(self, key):
    return self.db[key]

  def insert(self, key, data):
    self.db[key] = data
    
