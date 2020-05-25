"""Page index module."""
import urllib.request
from bs4 import BeautifulSoup


def get(webpath):
    """Request uri and get data."""
    with urllib.request.urlopen(webpath) as response:
        htmldoc = response.read()
        soup = BeautifulSoup(htmldoc, 'html.parser')

        return get_data(soup)


def get_data(soup):
    """Get page data."""
    data = {}
    data['categories'] = []

    dom_container = soup.find("div", class_="home-cat-container")

    for item in dom_container.find_all('div', class_="home-cat-container"):
        cat_obj = {}
        dom_title = item.find("div", class_="catrd-title")
        cat_obj['name'] = dom_title.find('a').string

        data['categories'].append(cat_obj)

    return data
