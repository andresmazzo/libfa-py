#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/')

from databases import db


class FA:
  def __init__(self):
    self.db = db.DB('fa')

  def importer(inputfilepath):
    # implement importer and convert data to db
    return

  def complete():
    # iterate db and get missing data from web reader
    return

  def exporter(outputdir):
    # implement exporter using db
    return
    