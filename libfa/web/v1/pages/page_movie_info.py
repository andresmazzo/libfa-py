"""Page movie info module."""
import urllib.request
import microdata


def get(webpath):
    """Request uri and get data."""
    with urllib.request.urlopen(webpath) as response:
        html = response.read()

        return get_data(html)


def get_data(html):
    """Get page data."""
    data = {}

    items = microdata.get_items(html)
    movie_item = items[0]
    data['microdata'] = movie_item

    return data
