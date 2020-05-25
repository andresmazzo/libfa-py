"""index page module."""


def get_data(soup):
    """get page data."""
    data = {}
    data['exported_at'] = soup.find("div", class_="download-ts").string

    dom_userprofile = soup.find("div", class_="profile-link")
    data['username'] = dom_userprofile.find("strong").string
    data['username_profile_url'] = dom_userprofile.find("a").string

    return data
