#!/usr/bin/python3

import sys
import os

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/')

from databases import db

from services.importers.zipdata import main as importer_expdata
from services.exporters.csv_v1 import main as exporter_csv

# FA Class integrates all libfa modules: importers, exporters and database
class FA:
  def __init__(self):
    self.db = db.DB('fa')

  def job_import(self, type, filepath):
    # implement importer and convert data to db
    data = importer_expdata.exec(filepath)

    self.db.insert('user', data)


  def complete(self):
    # iterate db and get missing data from web reader
    return


  def job_export(self, outputdir):
    # implement exporter using db
    data = db.get('user')['ratings']
    exporter_csv.ratings(data, outputdir)
    