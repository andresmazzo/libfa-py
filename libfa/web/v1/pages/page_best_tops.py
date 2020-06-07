"""Page index module."""
from bs4 import BeautifulSoup


def get(htmldoc):
    """Get page data."""
    soup = BeautifulSoup(htmldoc, 'html.parser')

    data = {}

    countries = []
    genres = []

    data['menu'] = {
        'countries': countries,
        'genres': genres
    }
    data['cards'] = []

    for card in soup.select(".best-tops > .wrap > .box"):
        obj = {}
        obj['slug'] = card['id']

        if len(card.div.contents) == 2:
            obj['type'] = 'country'
        else:
            obj['type'] = 'genre'

        obj['title'] = card.div.contents[len(card.div.contents)-1].string

        links = []
        for link in card.select("ul li"):
            links.append({
                'name': link.a.string,
                'url': link.a['href']
            })

        obj['links'] = links

        data['cards'].append(obj)

    return data
