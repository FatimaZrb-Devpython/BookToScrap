import requests
from bs4 import BeautifulSoup
import time
from book import *
from category import *
# import csv

def all_book (url):
    
    category = []

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
        
    list = soup.find("ul", class_='nav nav-list').find_all('li')
    for a in list :
        a =  a.find('a')
        link = a.get('href')
        category.append('https://books.toscrape.com/' + link)

time.sleep(1)
url = all_book('https://books.toscrape.com/index.html' )


# Créer une liste pour les en-têtes
# en_tete = ["home"]

# # Créer un nouveau fichier pour écrire dans le fichier appelé « category.csv »
# with open('all_book.csv', 'w') as csv_file:
#     # Créer un objet writer (écriture) avec ce fichier
#     writer = csv.writer(csv_file, delimiter=',')
#     writer.writerow(en_tete)
#     # Parcourir les éléments- zip permet d'itérer sur deux listes ou plus à la fois
#     for link in zip():
#         # Créer une nouvelle ligne pour chaque éléments à ce moment de la boucle
#         ligne = [link] 
#         writer.writerow(ligne)
        
