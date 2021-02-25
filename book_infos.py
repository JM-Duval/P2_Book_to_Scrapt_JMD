# -*-coding: utf-8 -*
""" This program is attached to the 'main.py' program. The target is find all information about
one book.
"""

import requests

from bs4 import BeautifulSoup


# --Title--------------------
def get_title(soup):
    title = soup.find('h1').text
    return title

# --UPC--universal_product_code------
def get_upc(soup):
    upc = soup.findAll('td')[0].text
    return upc

#--Price_including_tax---------------
def get_price_itax (soup):
    pit = soup.findAll ('td')[3].text[1:]
    return pit

#--Price_excluding_tax---------------
def get_price_etax (soup):
    pet = soup.findAll ('td')[2].text[1:]
    return pet

#--Number_available----
def get_available (soup):
    avail = soup.findAll ('td')[5].text
    return avail

#--product_of_description---
def get_description (soup):
    desc = soup.find('meta',{'name':'description'})['content'][5:-1]
    return desc

#--category------------------
def get_category (soup):
    category = soup.findAll('a')[3].text.replace(" ", "").replace("/n","")
    return category

#--number_of_review-----------
def get_nb_review (soup):
    nb_review = soup.findAll ('td')[6].text
    return nb_review

#--url_image-----------------
def get_img (soup):
    str_img = soup.img['src'].replace ('../..', 'http://books.toscrape.com')
    return str_img

#--dictionnary--------------

def get_book_infos (book_link):
    """Scrape information book and save in the dictionary"""
    book_dict = {}
    response = requests.get(book_link)
    soup = BeautifulSoup(response.text, "html.parser")
    book_dict['url'] = book_link
    book_dict['title'] = get_title(soup)
    book_dict['category'] = get_category(soup)
    book_dict['number of review'] = get_nb_review(soup)
    book_dict['url image'] = get_img(soup)
    book_dict['description'] = get_description(soup)
    book_dict['upc'] = get_upc(soup)
    book_dict['price excluding tax'] = get_price_etax(soup)
    book_dict['price including tax'] = get_price_itax(soup)
    book_dict['number available'] = get_available(soup)

    return book_dict

