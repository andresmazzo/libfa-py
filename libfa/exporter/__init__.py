#!/usr/bin/python3

import libfa.exporter.csv_v1.lists, libfa.exporter.csv_v1.ratings

def lists(name, filepath):
  # implement importer and convert data to db
  data = get_exporter(name).lists(filepath)

  return data
  # self.db.insert('user', data)


def get_exporter(name):
  dicts = {
      'csv_v1': libfa.dicts.csv_v1
  }  

  return dicts[name]