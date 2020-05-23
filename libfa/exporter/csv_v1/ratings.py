#!/usr/bin/python3

import sys
import csv


def ratings(data, outputFilepath):
  fp = open(outputFilepath, 'w')
  writer = csv.writer(fp)

  writer.writeRow(header())

  for item in data:
    if item.type == 'movie':
      writer.writerow(movie_data(item))
    elif item.type == 'tvshow':
      writer.writerow(tvshow_data(item))


def header():
  return [
    'FA ID',
    'Type',
    'Name',
    'Release Date',
    'Season Number',
    'Episode Number',
    'Rating'
    'Your Rating',
    'Date Rated'
  ]

def movie_data(obj):
  return [
    obj.id,
    'movie',
    obj.name,
  ]

def tvshow_data(obj):
  return [
    obj.id,
    'tvshow',
    obj.name
  ]