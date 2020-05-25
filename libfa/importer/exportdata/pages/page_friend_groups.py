"""friend_groups page module."""


def get_data(soup):
    """get data."""
    data = {}
    data['data'] = []

    dom_list = soup.find("table", class_="ml")

    for item in dom_list.find_all('tr'):
        tds = item.find_all('td')

        group = {}
        group['name'] = tds[0].find("a").string
        group['filepath'] = tds[0].find("a")['href']
        group['total'] = tds[1].string

        data['data'].append(group)

    return data
