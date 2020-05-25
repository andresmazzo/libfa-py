"""acccount_data page module."""


def get_data(soup):
    """get data."""
    data = {}
    data['data'] = []

    data['name'] = soup.title.string
    dom_list = soup.find("table", class_="ml")

    for item in dom_list.find_all('tr'):
        listobj = {}
        listobj['friend_name'] = item.find("td").string

        data['data'].append(listobj)

    return data
