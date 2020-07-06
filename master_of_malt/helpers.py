# Imports
import requests
from bs4 import BeautifulSoup


def get_pagination_links(url, html_class='list-paging'):
    """
    For a given url find the href attributes of anchor tags that match a certain HTML class.
    Returns a set of URLs.
    :param url: string, url to search for pagination links
    :param html_class: string, html class that identifies the links
    :return: list, return the other hrefs found with the given class
    """
    cookies = dict(
        MaOMa='VisitorID=556630649&IsVATableCountry=1&CountryID=464&CurrencyID=-1&CountryCodeShort=GB'
              '&DeliveryCountrySavedToDB=1')
    html = requests.get(url, headers={"Accept-Language": "en-GB"}, cookies=cookies).text
    soup = BeautifulSoup(html, features="html.parser")
    pagination = soup.find_all(class_=html_class)
    pagination_links = pagination[0].find_all('a')
    pagination_hrefs = [link.get('href') for link in pagination_links]
    return pagination_hrefs


def check_url_status_code(url, desired_status_code=200):
    """
    Check the status code for a given url when requested
    :param url: string, the url to request
    :param desired_status_code: int, the desired response status code
    :return: bool, does the response status code match desired_status_code
    """
    return requests.head(url).status_code == desired_status_code
