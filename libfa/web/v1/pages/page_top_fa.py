"""Page index module."""
from bs4 import BeautifulSoup


def get(htmldoc):
    """Get page data."""
    soup = BeautifulSoup(htmldoc, 'html.parser')

    data = {}
    data['movies'] = []

    for item in soup.select("#top-movies > li > ul"):
        movie_obj = {}
        movie_obj['id'] = item.find("div", class_="movie-card")['data-movie-id']
        movie_obj['avg_rating'] = item.find("div", class_="avg-rating")

        data['movies'].append(movie_obj)

    return data
