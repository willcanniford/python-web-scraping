# Imports
import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import random
import time
from helpers import get_pagination_links


# Set the master link 
url = "https://www.masterofmalt.com/gin/"

print(get_pagination_links("https://www.masterofmalt.com/gin/"))