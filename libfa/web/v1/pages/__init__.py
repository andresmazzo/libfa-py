"""Web V1 Pages module."""
from libfa.web.v1.pages import page_index, page_movie_info, page_top_fa, page_best_tops, page_search


def get_page(name: str, html):
    """Get an specified page."""
    dicts = {
        'index': page_index,
        'movie-info': page_movie_info,
        'top-fa': page_top_fa,
        'best-tops': page_best_tops,
        'search': page_search
    }

    page = dicts[name]

    return page.get(html)
