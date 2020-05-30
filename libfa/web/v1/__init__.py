"""Web V1 module."""
import importlib
import urllib.request
from libfa.web.v1.pages import get_page


# ---- getter functions

def movie(locale: str, id_attr):
    """Find movie by id."""
    result = get_page('movie-info', get_html(web_uri(locale, '/film' + id_attr + '.html')))

    # convert microdata to movie obj. Is this useful?
    return {
        'id': id_attr,
        'name': result['microdata'].name,
        'description': result['microdata'].description,
        'genre': result['microdata'].genre,
        'duration': result['microdata'].duration,
        'published_at': result['microdata'].datePublished
    }


def top_fa(locale: str):
    """Get the Top FilmAffinity."""
    return get_page('top-fa', get_html(web_uri(locale, '/topgen.php')))


def best_tops(locale: str):
    """Get the Best Tops."""
    return get_page('best-top', get_html(web_uri(locale, '/best_tops.php')))


def director(locale: str, name: str):
    """Find a director."""
    # TODO: Complete this faker example
    return get_page('search', get_html(web_uri(locale, '/search.html?name=' + name)))


def search(locale: str, param: str):
    """Search something."""
    # TODO: Complete this faker example
    return get_page('search', get_html(web_uri(locale, '/search.html?name=' + param)))


# ---- helper functions

def web_uri(locale: str, path: str):
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


def get_html(webpath: str):
    """Get html from webpath url."""
    with urllib.request.urlopen(webpath) as response:
        htmldoc = response.read()

        return htmldoc
