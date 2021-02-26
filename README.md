# P2_Book_to_Scrapt_JMD
# Programme de Scraping d'informations d'un site e-commerce.

Ce programme est une version beta d'un script permettant d'automatiser un système de surveillance des prix sur un site e-commerce de vente de livre : http://books.toscrape.com/. 

L'objectif est de récupérer les informations suivantes:

* product_page_url_

* universal_ product_code (upc)

* title

* price_including_tax

* price_excluding_tax

* number_available

* product_description

* category

* review_rating

* image_url


L'ensemble des données sont écrites dans un fichier CSV. Chaque CSV contient les informations des livres de la même catégorie et est classé dans un dossier unique. Dans ce même dossier, est créé un sous dossier contenant les images des couvertures de chaque livre.

## Pour commencer

Les instructions ci dessous vous aiderons à exécuter correctement ce programme. 

## Pré-requis 

* Python 3 installé ([Télécharger Python](https://www.python.org/downloads/)) 
* Savoir naviguer dans les dossiers & fichiers à partir d'un terminal.

## Installation

Pour un bon fonctionnement, il est préférable d'exécuter le programme dans un environnement virtuel.
Pour cela, ci dessous les étapes à suivre:

1. **Téléchargement du projet.**

    1. Depuis votre terminal, placez vous à l'endroit souhaité:
    
    ```cd [chemin d'accès]```  
    
    2. Creer un nouveau dossier:
    
    ```mkdir [nom de votre dossier]```
    
    3. Copier le programme source:
    
    ```git clone https://github.com/JM-Duval/P2_Book_to_Scrapt_JMD.git```
    
    Vous devez voir (depuis votre explorateur) les fichiers suivants:
        * main.py
        * all_book_in_category.py
        * all_category_link.py
        * requirements.txt
    

2. **Creer un environnement virtuel.**

    Depuis windows/mac/linux: ```python3 -m venv env```
    

3. **Activer l'environnement.**
    
    Depuis windows: ```env\Scripts\activate.bat```
    
    Depuis mac/linux: ```source env/bin/activate```
    
    Si vous rencontrez des difficultés ou si vous souhaitez plus de détails sur l'installation d'un environnement virtuel, vous pouvez vous reporter à la documentation Python:
    
    [Documentation Python](https://docs.python.org/fr/3.6/tutorial/venv.html/)  
    
4. **Installer les paquets.**

    ```pip install -r requirements.txt```

    En executant la commande: ```pip freeze```, vous devez voir apparaitre cette liste: beautifulsoup4==4.9.3 bs4==0.0.1 certifi==2020.12.5 chardet==4.0.0 idna==2.10 requests==2.25.1 soupsieve==2.2 tqdm==4.57.0 urllib3==1.26.3
    
5. **Lancement du programme**

    ```pyhton main.py```

    Des dossiers 'catégorie de livre' vont être généré à l'intérieur d'un unique dossier 'data'. Dans chaque dossier 'catégorie' est produit un fichier CSV contenant l'ensemble des données des livres, ainsi qu'un dossier image dans lequel se trouve toutes les images de couverture relative à ces mêmes livres.


## Fabriqué avec
[PyCharm Community Edition 2020.2.3 x64] (https://pycharm-community-edition.fr.softonic.com/) - Editeur de textes


## Auteurs

* **JM Duval** 


## Remerciements

Merci à **Ranga Gonnage** pour ses conseils et sa diplomatie. 
