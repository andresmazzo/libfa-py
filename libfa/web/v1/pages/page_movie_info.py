"""Page movie info module."""
import microdata


def get(htmldoc):
    """Get page data."""
    data = {}

    items = microdata.get_items(htmldoc)
    movie_item = items[0]
    data['microdata'] = movie_item

    return data
