# -*-coding: utf-8 -*
# Script permettant de scraper les informations d'une catégorie d'ouvrage

# Import libraries
import requests
import csv
from bs4 import BeautifulSoup
from math import *

#--link_all_book_in_category______________--
def get_all_book_in_category (category_link):
        #print (category_link)
        print (category_link)
        response = requests.get(category_link)
        soup = BeautifulSoup(response.text, "html.parser")
        # --Pagination---------------
        page = soup.find('form',{'method':'get'}).text
        result= page[3:5]
        affich= page[29:31]
        book_links = []
        if int(result) > 20 :
                nb_page = ceil(int(result) / int(affich))
                #print (nb_page)
                #print ('Nombre de page: ',nb_page)
                for x in range (1, nb_page+1):
                        url = category_link[:-6]
                        #print (x)
                        url_comp = url + str(x) + str('.html')
                        #print (url_comp)
                        response1 = requests.get(url_comp)
                        soup1 = BeautifulSoup(response1.text, "html.parser")
                        h3 = soup1.findAll('h3')
                        for ahref in h3:
                                url_book = ahref.find('a').get('href').replace('../../..','http://books.toscrape.com/catalogue')
                                book_links.append(url_book)

                        x += 1

                return book_links
        else:
                response2 = requests.get(category_link)
                soup1 = BeautifulSoup(response2.text, "html.parser")
                h3 = soup1.findAll('h3')
                for ahref in h3:
                        url_book = ahref.find('a').get('href').replace('../../..','http://books.toscrape.com/catalogue')
                        book_links.append(url_book)

                return book_links

# Script test
#r = get_all_book_in_category(url_cat)
#print (r)
#url_cat = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html'
#response = requests.get(url_cat)

# --Create a BeautifulSoup object----------------------
#soup = BeautifulSoup(response.text, "html.parser")






