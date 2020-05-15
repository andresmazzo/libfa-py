
# Wrapper for Beatiful Soap or other html reader package

from bs4 import BeautifulSoup


def load(htmldoc):
  return Htmlr(htmldoc)
  

class Htmlr(object):
    soup = ''

    def __init__(self, htmldoc):
      self.soup = BeautifulSoup(htmldoc, 'html.parser')

    def lib(self):
      return self.soup
