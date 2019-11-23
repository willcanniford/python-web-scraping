# Imports
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Define the class for a player
class CricketPlayer:
    def __init__(self, innings_by_innings_link):
        self.link = innings_by_innings_link
        self.soup = BeautifulSoup(requests.get(innings_by_innings_link).text, features="html.parser")
        
    def view_raw_html(self):
        return(self.soup)
    
    def innings(self):
        for caption in self.soup.find_all('caption'):
            if caption.get_text() == 'Innings by innings list':
                main_table = caption.find_parent('table', {'class': 'engineTable'})
                
        columns = [header.get_text() for header in main_table.find('thead').find_all('tr')[0].find_all('th')]
        rows = []

        for innings in [row for row in main_table.find('tbody').find_all('tr')]:
            rows.append([stat.get_text() for stat in innings.find_all('td')])
            
        return(pd.DataFrame(rows, columns=columns))