# -*-coding: utf-8 -*
# main Script de book_to_Scrapt

# --import_libraries-----------------------------------
import requests
import csv
from bs4 import BeautifulSoup
from book_infos import get_book_infos
from all_book_in_category import get_all_book_in_category
from all_category_link import get_all_category_link
from pathlib import Path
import pathlib
import os

# -----------------------------------------------------
url_bts = 'http://books.toscrape.com/'
response = requests.get(url_bts)
# --Create_a_BeautifulSoup_object----------------------
soup = BeautifulSoup(response.text, "html.parser")


# --Data_Path----------------------
data = Path('data')
if not os.path.exists(data):  # if data-(Path) don't exist, create data-(Path)
        os.mkdir(data)

# --Category_Path------------------
uls = soup.findAll('a')[3:-41]
#print (uls)
for a_tag in uls:
        category_folder = a_tag.attrs.get("href")[25:-13].replace("_", "").replace ("\n",",").replace('-','') #find all category
        # -- CSV_Path -------------------------------
        dir_cat = os.path.join(data, category_folder)
        if not os.path.exists(dir_cat):  # if dir_cat don't exist, create dir_cat
                os.mkdir(dir_cat)
        # -- Image_Path -----------------------------
        img_path = os.path.join(dir_cat, 'image')
        if not os.path.exists(img_path):  # if dir_cat don't exist, create dir_cat
                os.mkdir(img_path)


# --Create_CSV --------------------------------------
def create_csv(book):

        category = book['category']  # information given by book_infos
        with open (os.stat(nom de fichier) os.path.join(data, category , category+ '.csv'), 'a', newline='', encoding="utf-8-sig") as file:
                ecrire = csv.writer (file, delimiter= ',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
                ecrire.writerow(book.values())

# --Download_image---------------------
def record_image (book):
        title = book['title'][:8].replace('"', "")  # information given by book_infos
        category = book['category']  # information given by book_infos
        url_img = book['url image']  # information given by book_infos
        url_image = requests.get(url_img)  # requests for catch imgae
        with open(os.path.join(data, category , 'image' , title + '.jpeg'), 'wb') as f:
                f.write(url_image.content)



# --Main_Script--------------------------------------
#if __name__ == '__main__':
category_links = get_all_category_link(url_bts) # tous les liens des catégories
for category_link in category_links:
        book_links = get_all_book_in_category(category_link) # tous les livres par catégorie
        for book_link in book_links:
                book = get_book_infos(book_link)  # information given by book_infos
                create_csv(book)
                record_image(book)