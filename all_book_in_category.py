# -*-coding: utf-8 -*
""" This program is attached to the 'main.py' program. The target is find all
the links of books in category.
"""

import requests

from bs4 import BeautifulSoup
from math import ceil


def get_all_book_in_category(category_link):
    """link all book in category"""
    response = requests.get(category_link)
    soup = BeautifulSoup(response.text, "html.parser")
    # --Pagination---------------
    page = soup.find('form', {'method': 'get'}).text
    result = page[3:5]
    affich = page[29:31]
    book_links = []
    if int(result) > 20:
        nb_page = ceil(int(result) / int(affich))
        for page in range(1, nb_page + 1):
            url = category_link[:-10]
            url_comp = url + 'page-' + str(page) + str('.html')
            response1 = requests.get(url_comp)
            soup1 = BeautifulSoup(response1.text, "html.parser")
            h3 = soup1.findAll('h3')
            for ahref in h3:
                url_book = ahref.find('a').get('href') \
                    .replace('../../..', 'http://books.toscrape.com/catalogue')
                book_links.append(url_book)
            page += 1

        return book_links
    else:
        response2 = requests.get(category_link)
        soup1 = BeautifulSoup(response2.text, "html.parser")
        ss_title = soup1.findAll('h3')
        for ahref in ss_title:
            url_book = ahref.find('a').get('href') \
                .replace('../../..', 'http://books.toscrape.com/catalogue')
            book_links.append(url_book)

        return book_links
