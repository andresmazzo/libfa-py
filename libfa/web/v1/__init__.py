"""Web V1 module."""
import urllib.request
import urllib.parse as urlparse
from urllib.parse import urlencode

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


def top_fa(locale: str, params: dict):
    """Get the Top FilmAffinity."""
    # ?genre=&country=&notvse=1&fromyear=&toyear=&nodoc=1
    result = get_page('top-fa', get_html(web_uri(locale, '/topgen.php', params)))

    return result['movies']


def best_tops(locale: str):
    """Get the Best Tops."""
    result = get_page('best-tops', get_html(web_uri(locale, '/best_tops.php', {})))

    return result


def search(locale: str, params: dict):
    """Search something."""
    # ?stext=&stype=cast
    # stype support: title|cast|director
    result = get_page('search', get_html(web_uri(locale, '/search.php', params)))

    return result['data']


# ---- helper functions

def web_uri(locale: str, path: str, params: dict = {}):
    """Get uri."""
    # add params to url
    # https://stackoverflow.com/questions/2506379/add-params-to-given-url-in-python
    url_parts = list(urlparse.urlparse(base_uri() + '/' + locale + path))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    # Thanks for quote_via arg. recomendation
    # https://stackoverflow.com/questions/21823965/use-20-instead-of-for-space-in-python-query-parameters
    url_parts[4] = urlencode(query, quote_via=urllib.parse.quote)

    return urlparse.urlunparse(url_parts)


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
