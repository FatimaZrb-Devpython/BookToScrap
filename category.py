import requests
from bs4 import BeautifulSoup
import csv

def category ():
    url = "https://books.toscrape.com/catalogue/category/books/poetry_23/index.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    lists = soup.find("ol", class_='row')
    list = []
    for list in lists : 
            a = lists.findAll('a')
            link = a['href']
            list.append('https://books.toscrape.com/catalogue/category/books/poetry_23/index.html' + link)
            print(list)


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
        
category()
