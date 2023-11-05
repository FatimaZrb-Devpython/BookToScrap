import requests
from bs4 import BeautifulSoup
import time
from book import *
# import csv

def category ():
    
    list = []

    for i in range (1,9) : 
        url = 'https://books.toscrape.com/catalogue/category/books/default_15/page-' + str(i) + '.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        row = soup.find("ol", class_='row').find_all('h3')
        for a in row :
            a =  a.find('a')
            link = a.get('href')
            link = link.replace('../../..','')
            list.append('https://books.toscrape.com/catalogue' + link)
            print(list)

time.sleep(1)
category()


# # Créer une liste pour les en-têtes
# en_tete = ["list"]

# # Créer un nouveau fichier pour écrire dans le fichier appelé « category.csv »
# with open('category.csv', 'w') as csv_file:
#     # Créer un objet writer (écriture) avec ce fichier
#     writer = csv.writer(csv_file, delimiter=',')
#     writer.writerow(en_tete)
#     # Parcourir les éléments- zip permet d'itérer sur deux listes ou plus à la fois
#     for list in zip(list):
#         # Créer une nouvelle ligne pour chaque éléments à ce moment de la boucle
#         ligne = [list] 
#         writer.writerow(ligne)
        
