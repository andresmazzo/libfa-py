"""Web V1 module."""
import importlib
import urllib.request
from libfa.web.v1.pages import get_page


# ---- getter functions

def movie(locale: str, id_attr):
    """Find movie by id."""
    result = get_page('movie-info', get_html(web_uri(locale, '/film' + id_attr + '.html')))

    actors = []
    for item in result['microdata'].get_all('actor'):
        actor = {
            'url': item.url,
            'name': item.name,
        }
        actors.append(actor)

    rating = {
        'value': result['microdata'].aggregateRating.ratingValue,
        'best': result['microdata'].aggregateRating.bestRating,
        'worst': result['microdata'].aggregateRating.worstRating,
        'review_count': result['microdata'].aggregateRating.reviewCount,
        'rating_count': result['microdata'].aggregateRating.ratingCount,
    }

    reviews = []
    for item in result['microdata'].get_all('review'):
        review = {
            'description': item.reviewBody,
            'author': item.author,
        }
        reviews.append(review)

    return {
        'id': id_attr,
        'name': result['microdata'].name,
        'description': result['microdata'].description,
        'director': {
            'url': result['microdata'].director.url,
            'name': result['microdata'].director.name,
        },
        'actors': actors,
        'duration': result['microdata'].duration,
        'genres': result['microdata'].get_all('genre'),
        'published_at': result['microdata'].datePublished,
        'rating': rating,
        'reviews': reviews
    }


def top_fa(locale: str):
    """Get the Top FilmAffinity."""
    result = get_page('top-fa', get_html(web_uri(locale, '/topgen.php')))

    return result['movies']


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
