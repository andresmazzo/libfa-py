"""Page index module."""
from bs4 import BeautifulSoup


def get(htmldoc):
    """Get page data."""
    soup = BeautifulSoup(htmldoc, 'html.parser')

    data = {}
    data['categories'] = []

    dom_container = soup.find("div", class_="home-cat-container")

    for item in dom_container.find_all('div', class_="home-cat-container"):
        cat_obj = {}
        dom_title = item.find("div", class_="catrd-title")
        cat_obj['name'] = dom_title.find('a').string

        data['categories'].append(cat_obj)

    return data
