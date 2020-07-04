# Imports
import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import random
import time


def get_pagination_links(url, html_class = 'list-paging'):
    """
    For a given url find the href attributes of anchor tags that match a certain HTML class.
    Returns a set of URLs.
    """
    cookies = dict(MaOMa='VisitorID=556630649&IsVATableCountry=1&CountryID=464&CurrencyID=-1&CountryCodeShort=GB&DeliveryCountrySavedToDB=1')
    html = requests.get(url, headers = {"Accept-Language": "en-GB"}, cookies = cookies).text 
    soup = BeautifulSoup(html, features="html.parser")
    pagination = soup.find_all(class_= html_class)
    pagination_links = pagination[0].find_all('a')
    
    # Return a set of distinct URLs 
    return [link.get('href') for link in pagination_links]

