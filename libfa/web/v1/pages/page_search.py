"""Page index module."""
from bs4 import BeautifulSoup


def get(htmldoc):
    """Get page data."""
    soup = BeautifulSoup(htmldoc, 'html.parser')

    data = {}
    data['data'] = []

    for item in soup.select("#mt-content-cell .z-search > .se-it"):
        card_elem = item.find("div", class_="movie-card")

        obj = {}
        obj['id'] = card_elem['data-movie-id']
        obj['title'] = card_elem.select(".mc-info-container .mc-title a")[0].string
        # TODO: Support movies with multiple directors
        obj['director'] = card_elem.select(".mc-info-container  .mc-director a")[0].string

        data['data'].append(obj)

    return data
