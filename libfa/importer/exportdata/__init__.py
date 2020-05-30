"""Importer exportdata module."""

import sys
import os
from zipfile import ZipFile

from libfa.importer.exportdata.pages import get_page


def support():
    """Returns the supported pages."""
    return ['index', 'account-data', 'movie-ratings', 'lists', 'friend-groups']


def run(filepath: str):
    """Exec importer for an specified zip file."""
    output_dir = 'temp'
    with ZipFile(filepath, 'r') as zip_obj:
        zip_obj.extractall(output_dir)

    data = get_all(output_dir)
    # TODO: Delete temp dir

    return data


def get_all(basepath: str):
    """Returns data from all pages."""
    data = {}

    data['pages'] = {}
    data['pages']['index'] = get_page('index', basepath + '/index.html')
    data['pages']['account-data'] = get_page(
        'account-data', basepath + '/html/account-data.html')
    data['pages']['movie-ratings'] = get_page(
        'movie-ratings', basepath + '/html/movie-ratings.html')
    data['pages']['lists'] = get_page('lists', basepath + '/html/lists.html')
    data['pages']['friend-groups'] = get_page(
        'friend-groups', basepath + '/html/friend-groups.html')

    data['sections'] = {}

    data['sections']['list'] = []
    for list_data in data['pages']['lists']['data']:
        page_data = get_page('list', basepath + '/html/' + list_data['url'])
        data['sections']['list'].append(page_data)

    data['sections']['friend-group'] = []
    for friend_group_data in data['pages']['friend-groups']['data']:
        page_data = get_page('friend-group', basepath +
                             '/html/' + friend_group_data['filepath'])
        data['sections']['friend-group'].append(page_data)

    # TODO: Support all features (im threads, ignore movies, etc)

    return data
