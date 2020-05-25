"""list page module."""


def get_data(soup):
    """get page data."""
    data = {}
    data['data'] = []

    data['name'] = soup.title.string
    dom_list = soup.find("table", class_="lists")

    for item in dom_list.find_all('tr'):
        listobj = {}
        listobj['number'] = item.find('th').string
        listobj['movie_name'] = item.find("td").string

        data['data'].append(listobj)

    return data
