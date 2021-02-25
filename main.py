# -*-coding: utf-8 -*
""" This program is a beta version of a script to automate a price monitoring
system on a website. The target is to retrieve information from each book and
write it to a CSV file. And more, this script download the picture of the plate
book for each book.
"""

import os
import csv
import requests

from bs4 import BeautifulSoup
from pathlib import Path
from tqdm import tqdm
from book_infos import get_book_infos
from all_category_link import get_all_category_link
from all_book_in_category import get_all_book_in_category


url_bts = "http://books.toscrape.com/"
response = requests.get(url_bts)
soup = BeautifulSoup(response.text, "html.parser")

# Data_Path
data = Path("data")
if not os.path.exists(data):
    os.mkdir(data)

# Category_Path
uls = soup.findAll("a")[3:-41]
for a_tag in uls:
    category_folder = (
        a_tag.attrs.get("href")[25:-13]
        .replace("_", "")
        .replace("\n", ",")
        .replace("-", "")
    )
    # CSV_Path
    dir_cat = os.path.join(data, category_folder)
    if not os.path.exists(dir_cat):
        os.mkdir(dir_cat)
    # Image_Path
    img_path = os.path.join(dir_cat, "image")
    if not os.path.exists(img_path):
        os.mkdir(img_path)


def create_csv(book):
    """Information from book_infos.py"""
    category = book["category"]
    if not os.path.isfile(os.path.join(data, category, category + ".csv")):
        with open(os.path.join(data, category, category + ".csv"), "a",
                  newline="", encoding="utf-8-sig") as file:
            csv_writer = csv.DictWriter(file, fieldnames=book.keys(),
                                        delimiter=",")
            csv_writer.writeheader()
            csv_writer.writerow(book)
    else:
        with open(os.path.join(data, category, category + ".csv"), "a",
                  newline="", encoding="utf-8-sig") as file:
            csv_writer = csv.writer(file, delimiter=",", quotechar=" ",
                                    quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(book.values())


def record_image(book):
    """Download image"""
    title = book["title"][:8].replace('"', "").replace(":", "_").replace("/",
                                                                         "")
    category = book["category"]
    url_img = book["url image"]
    url_image = requests.get(url_img)
    with open(os.path.join(data, category, "image", title + ".jpeg"),
              "wb") as file:
        file.write(url_image.content)


# Main_Script
if __name__ == "__main__":
    category_links = get_all_category_link(url_bts)
    for category_link in tqdm(category_links):
        book_links = get_all_book_in_category(category_link)
        for book_link in book_links:
            book = get_book_infos(book_link)
            create_csv(book)
            record_image(book)
