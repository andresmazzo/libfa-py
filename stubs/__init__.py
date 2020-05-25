
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def get_html(filename):
    path = os.path.join(__location__, filename + '.html')

    return open(path, 'r').read()
