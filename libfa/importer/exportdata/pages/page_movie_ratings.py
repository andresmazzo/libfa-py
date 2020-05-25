"""movie_ratings page module."""


def get_data(soup):
    """get page data."""
    data = {}
    data['data'] = []

    dom_list = soup.find("table", class_="movie-ratings")

    for item in dom_list.find_all('tr'):
        tds = item.find_all('td')
        rating = {}
        rating['value'] = tds[0].find("div", class_="user-rating").string
        rating['movie_name'] = tds[1].string
        rating['created_at'] = tds[2].string

        data['data'].append(rating)

    return data
