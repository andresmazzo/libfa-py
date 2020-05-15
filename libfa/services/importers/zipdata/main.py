#!/usr/bin/python3

import sys
from zipfile import ZipFile

import os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../../readers/html/exportdata')

import index as lindex
import movie_ratings as lmovieratings
import lists as llists
import account_data as laccountdata
import friend_groups as lfriendgroups


def exec(inputZipFilepath):
  outputDir = 'temp'
  extractZip(inputZipFilepath, outputDir)
  db = loadDir(outputDir)
  # TODO: Delete temp dir

  return db


def extractZip(inputFile, outputDir):
  with ZipFile(inputFile, 'r') as zipObj:
    zipObj.extractall(outputDir)


def loadDir(dir):
  zipdb = {}

  zipdb['index'] = lindex.get(dir + '/index.html')
  zipdb['movie_ratings'] = lmovieratings.get(dir + '/html/movie-ratings.html')
  zipdb['lists'] = llists.get(dir + '/html/lists.html')
  zipdb['account_data'] = laccountdata.get(dir + '/html/account-data.html')
  zipdb['friend_groups'] = lfriendgroups.get(dir + '/html/friend-groups.html')

  # TODO: Iterate lists and friend groups to get detail of each.
  # TODO: Load all dir content

  return zipdb