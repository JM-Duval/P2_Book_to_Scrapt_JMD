# -*-coding: utf-8 -*
""" This program is attached to the 'main.py' program. The target is find all the links of all
categories.
"""


import requests
import csv
from bs4 import BeautifulSoup

# --All_category_links---------------------------------
def get_all_category_link(url_bts):
        response = requests.get(url_bts)
        soup = BeautifulSoup(response.text, "html.parser")
        uls=soup.findAll ('a')[3:-41]
        category_dict = []
        for a_tag in uls:
                add_url = 'http://books.toscrape.com/'
                cat_links = add_url+a_tag.attrs.get("href")
                category_dict.append(cat_links)

        return category_dict
