import requests
from bs4 import BeautifulSoup
import csv

def get_all_categories (url):
    
    categories = []

    response = requests.get(url, timeout=(10, 30))
    soup = BeautifulSoup(response.content, 'html.parser')
        
    list = soup.find("ul", class_='nav nav-list').find_all('li')
    for a in list :
        a =  a.find('a')
        link = a.get('href')
        url_book = ('https://books.toscrape.com/' + link)
        split = url_book.split('/')
        title_category = split[6]
        categories.append(('title : ',title_category, 'url :',url_book))
        
    return categories 


def save_categories (categories) : 

    # Créer une liste pour les en-têtes
    en_tete = ["category"]

    # Créer un nouveau fichier pour écrire dans le fichier appelé « category.csv »
    with open('all_categories.csv', 'w') as csv_file:
        # Créer un objet writer (écriture) avec ce fichier
        writer = csv.writer(csv_file, delimiter=';')
        writer.writerow(en_tete)

        # Créer une nouvelle ligne pour chaque éléments à ce moment de la boucle
        writer.writerow(categories) 
        
        
