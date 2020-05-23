#!/usr/bin/python3

import sys
import os

import libfa.importer.exportdata

def run(name, filepath):
  # implement importer and convert data to db
  data = get_importer(name).exec(filepath)

  return data
  # self.db.insert('user', data)


def get_importer(name):
  importers_dict = {
      'exportdata': libfa.importer.exportdata
  }  

  return importers_dict[name]