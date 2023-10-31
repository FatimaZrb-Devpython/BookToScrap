import requests
from bs4 import BeautifulSoup
import time
# import csv

def category (url):
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    row = soup.find("ol", class_='row')
    lists = row.find_all('a')
    list = []
    for a in lists : 
            link = a.get('href')
            link = link.replace('../../..','')
            list.append('https://books.toscrape.com/catalogue' + link)

time.sleep(3)
            
url = category("https://books.toscrape.com/catalogue/category/books/poetry_23/index.html")


# # Créer une liste pour les en-têtes
# en_tete = ["link"]

# # # Créer un nouveau fichier pour écrire dans le fichier appelé « category.csv »
# with open('category.csv', 'w') as csv_file:
# #     # Créer un objet writer (écriture) avec ce fichier
#     writer = csv.writer(csv_file, delimiter=',')
#     writer.writerow(en_tete)
# #     # Parcourir les éléments- zip permet d'itérer sur deux listes ou plus à la fois
#     for link in zip(links):
# #         # Créer une nouvelle ligne pour chaque éléments à ce moment de la boucle
#         ligne = [link] 
#         writer.writerow(ligne)
        
