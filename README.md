  
    Book to Scrape
Ce programme est une version beta d'un script permettant d'automatiser un système de surveillance des prix sur un site web : http://books.toscrape.com/. 
A partir de ce site, l'objectif est de récupérer les informations de chaque livre et de les écrire dans un fichier CSV. Chaque CSV contient les informations des livres de la même catégorie et est classé dans un dossier uniquement. Dans ce même dossier, est créé un sous dossier contenant les images des  couvertures de chaque livre.

    Pré-requis
Conaissance minimum en:
_Python (fonctionnement, architecture, struture).
_Git Hub (connaitre les fonctions de basse)
_Git Bash (naviguer dans les dossiers, fichiers de l'explorateur)

    Installation

1-(GitHub) Depuis le projet 'P2_Book_to_Scrapt_JMD' (https://github.com/JM-Duval/P2_Book_to_Scrapt_JMD), cliquer sur la fonction 'code' puis copier le lien https. 
2-(Explorateur) A l'endroit ou vous souhaitez, créer un nouveau dossier.
3-(Git Bash) A partir de Git Bash, placez vous sur le dossier contenant vos fichiers. 
4-(Git Bash) Une fois sur votre dossier, cloner le dossier à l'aide la commande 'git clone' + le lien du dossier Git Bash.
5-(Explorateur) Vérifier que vous avez bien l'ensemble des 6 dossiers ont bien été copié en local dans votre dossier.
6-(Git Bash) Creer un environnement virtuel à l'aide de la commande 'python -m venv env'.
7-(Git Bash) Activer l'environnement virtuel à l'aide de la commande 'env/bin/activate' >> sous linus et 'env/Scripts/activate.bat' >> sous Windows. À ce stade, votre terminal (selon celui que vous utilisez) ajoutera le nom de votre environnement au début de chaque ligne de votre terminal (ici, ‘env’)
8-(Git Bash) Revenez sur votre dossier principal puis excécuter la commande 'pip install -r requirements.txt' pour installer les pacquets nécessaires
9-(Git Bash) Lancer le programme 'main.py'
 
    Programmes & Ressources

_Git Bash
_PyCharm Community Edition 2020.2.3 x64
_Python 3

    Auteurs

JM_Duval


# P2_Book_to_Scrapt_JMD
# Programme de Scraping d'informations d'un e-commerce

Ce programme est une version beta d'un programme permettant d'automatiser un système de surveillance des prix sur un site e-commerce de vente de livre : http://books.toscrape.com/. 

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


L'ensemble des données sont écrit dans un fichier CSV. Chaque CSV contient les informations des livres de la même catégorie et est classé dans un dossier unique. Dans ce même dossier, est créé un sous dossier contenant les images des couvertures de chaque livre.

## Pour commencer

Les instructions ci dessous vous aiderons à exécuter correctement ce programme. 

## Pré-requis 

* Python 3 installé ([Télécharger Python](https://www.python.org/downloads/)) 
* Savoir naviguer dans les dossiers & fichiers à partir d'un terminal.

## Installation

Pour un bon fonctionnement, il est préférable d'exécuter le programme dans un environnement virtuel.
Voici le détail des étapes à suivre:

1. Téléchargement du projet

    **Depuis votre terminal, placez vous à l'endroit souhaité:** 
    
    ```cd [chemin d'accès]```  
    
    **Creer un nouveau dossier:**
    
    ```mkdir [nom de votre dossier]```
    
    **Copier le programme source:**
    
    ```git clone https://github.com/JM-Duval/P2_Book_to_Scrapt_JMD.git```
    
    **Vous devez voir (depuis votre explorateur) les fichiers suivants:**
    * main.py
    * all_book_in_category.py
    * all_category_link.py
    * requirements.txt
    

3. Creer un environnement virtuel

    **Depuis windows/mac/linux:** ```python3 -m venv env```
    

4. Activer l'environnement
    
    **Depuis windows:** ```env\Scripts\activate.bat```
    
    **Depuis mac/linux:** ```source env/bin/activate```
    
    Si vous rencontrez des difficultés ou pour plus de détails sur l'installation d'un environnement virtuel, vous pouvez vous reporter à la documentation Python:
    
         [Documentation Python](https://docs.python.org/fr/3.6/tutorial/venv.html/)  
    
    
