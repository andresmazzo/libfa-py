"""Web V1 module."""
import importlib

from libfa.web.v1.pages import get_page


def movie(locale, id_attr):
    """Find movie by id."""
    return get_page('movie-info', web_uri(locale, '/film' + id_attr + '.html'))


def top_fa(locale):
    """Get the Top FilmAffinity."""
    return get_page('movie-info', web_uri(locale, '/topgen.html'))


def best_top(locale):
    """Get the Best Top."""
    return get_page('best-top', web_uri(locale, '/best_top.html'))


def director(locale, name):
    """Find a director."""
    # TODO: Complete this faker example
    return get_page('search', web_uri(locale, '/search.html?name=' + name))


def search(locale, param):
    """Search something."""
    # TODO: Complete this faker example
    return get_page('search', web_uri(locale, '/search.html?name=' + param))


def web_uri(locale, path):
    """Get uri."""
    return base_uri() + '/' + locale + path


def locales():
    """Get supported locales."""
    return [
        'ar',  # argentina
        'au',  # australia
        'bo',  # bolivia
        'ca',  # canada
        'cl',  # chile
        'co',  # colombia
        'cr',  # costa rica
        'ec',  # ecuador
        'es',  # spain
        'ie',  # irland
        'mx',  # mexico
        'pe',  # peru
        'uk',  # united kingdom
        'us',  # united states
        'uy',  # uruguay
        've',  # venezuela
    ]


def base_uri():
    """Get base uri."""
    return 'https://www.filmaffinity.com'
