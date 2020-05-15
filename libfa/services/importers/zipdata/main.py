#!/usr/bin/python3

import sys
from zipfile import ZipFile

import os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../../readers/html/exportdata')

import index as lindex
import movie_ratings as lmovieratings


def exec(inputZipFilepath):
  outputDir = 'temp'
  extractZip(inputZipFilepath, outputDir)
  loadDir(outputDir)
  # TODO: Delete temp dir



def extractZip(inputFile, outputDir):
  with ZipFile(inputFile, 'r') as zipObj:
    zipObj.extractall(outputDir)


def loadDir(dir):
  lindex.load(dir + '/index.html')
  lmovieratings.load(dir + '/html/movie-ratings.html')
  # TODO: Load all dir content