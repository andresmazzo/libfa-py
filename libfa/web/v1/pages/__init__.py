"""Web V1 Pages module."""
from libfa.web.v1.pages import page_index, page_movie_info


def get_page(name, filepath):
    """Get an specified page."""
    dicts = {
        'index': page_index,
        'movie-info': page_movie_info
    }

    page = dicts[name]

    return page.get(filepath)
