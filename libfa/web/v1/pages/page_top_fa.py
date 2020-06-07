"""Page index module."""
from bs4 import BeautifulSoup


def get(htmldoc):
    """Get page data."""
    soup = BeautifulSoup(htmldoc, 'html.parser')

    data = {}
    data['movies'] = []

    for item in soup.select("#top-movies > li > ul"):
        card_elem = item.find("div", class_="movie-card")
        title_elem = card_elem.find("div", class_="mc-title")

        movie_obj = {}
        movie_obj['id'] = card_elem['data-movie-id']
        movie_obj['title'] = title_elem.contents[0]['title']
        movie_obj['year'] = title_elem.contents[1].string
        movie_obj['flag'] = title_elem.contents[2]['src']

        movie_obj['avg_rating'] = item.find("div", class_="avg-rating").string
        movie_obj['rat_count'] = item.find("div", class_="rat-count").contents[0]

        data['movies'].append(movie_obj)

    return data
