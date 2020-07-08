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


def check_url_status_code(url: str, cookies: dict = {}, headers: dict = {}, desired_status_code: int = 200) -> bool:
    """
    Check the status code for a given url when requested
    :rtype: bool
    :param cookies: dict, headers to pass to the requests.head call
    :param headers: dict, cookies to pass to the requests.head call
    :param url: string, the url to request
    :param desired_status_code: int, the desired response status code
    :return: bool, does the response status code match desired_status_code
    """
    return requests.get(url, cookies=cookies, headers=headers).status_code == desired_status_code


def check_page_exists(url: str, cookies: dict = {}, headers: dict = {}):
    """
    Check whether a given URL can be reached, even after redirects
    :param headers: dict, headers to pass to requests.get
    :param url: str, the url to check
    :param cookies: dict, cookies to pass to requests.get
    :return: bool, whether the url provided was found
    """
    response = requests.get(url, cookies=cookies, headers=headers)

    if response.history:
        # The URL was redirected, but you ended up at the given url
        return response.status_code == 200 and response.url == url
    else:
        return response.status_code == 200
