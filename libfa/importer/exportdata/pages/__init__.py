"""Web V1 Pages module."""
from bs4 import BeautifulSoup
from libfa.importer.exportdata.pages import page_index, page_account_data
from libfa.importer.exportdata.pages import page_movie_ratings
from libfa.importer.exportdata.pages import page_list, page_lists
from libfa.importer.exportdata.pages import page_friend_group, page_friend_groups


def get_page(name, filepath):
    """Get page by name."""
    pages_dict = {
        'index': page_index,
        'account-data': page_account_data,
        'movie-ratings': page_movie_ratings,
        'list': page_list,
        'lists': page_lists,
        'friend-group': page_friend_group,
        'friend-groups': page_friend_groups
    }

    page_reader = pages_dict[name]

    return page_reader.get_data(load_html(filepath))


def load_html(filepath):
    """Load html with soup."""
    htmldoc = open(filepath, 'r').read()
    soup = BeautifulSoup(htmldoc, 'html.parser')

    return soup
