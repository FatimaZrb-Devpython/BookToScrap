import requests
from bs4 import BeautifulSoup
import csv
import os
import re


def get_books_one_category (category):
    
    url = category[1]
    url_split = url.split('/')
    path = '/'.join(url_split[:-1])
    
    response = requests.get(url, timeout=(10, 30))
    soup = BeautifulSoup(response.content, 'html.parser')

    books = []

    row = soup.find("ol", class_='row').find_all('h3')
    for a in row :
        a =  a.find('a')
        link = a.get('href')
        link = link.replace('../../../','')
        books.append( 'https://books.toscrape.com/catalogue'+ '/' + link)
        
    try:
            
        next = soup.find('ul', class_= 'pager').find('li', class_='next')
        while next != None :
            current_url = ""
            for a in next : 
                a = next.find('a')
                link_next = a.get('href')
                current_url = path + '/' +  link_next
                
            response = requests.get(current_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            next_row = soup.find("ol", class_='row').find_all('h3')
            for a in next_row :
                a =  a.find('a')
                link = a.get('href')
                link = link.replace('../../../','')
                books.append('https://books.toscrape.com/catalogue' + '/' + link)
                
            next = soup.find('ul', class_= 'pager').find('li', class_='next')
    except: 
        return books
    
    return books



def save_books_category(books, category):
    
        category= category[0]

       # Construire le chemin du dossier de la catégorie
        category_folder = fr'./categories/{category}'

        # Créer le dossier de la catégorie s'il n'existe pas
        os.makedirs(category_folder, exist_ok=True)

        # Construire le chemin du fichier dans le dossier de la catégorie
        file_path = os.path.join(category_folder, f'{category}.csv')

        # Vérifier si le fichier existe déjà
        file_exists = os.path.isfile(file_path)

        # Créer un nouveau fichier pour écrire dans le fichier appelé « category_title.csv »
        with open(file_path, 'w') as csv_file:
            # Créer un objet writer (écriture) avec ce fichier
            writer = csv.writer(csv_file, delimiter=',')

            # Si le fichier n'existe pas, écrire les en-têtes
            if not file_exists:
                en_tete = [category]
                writer.writerow(en_tete)

            # Écrire chaque livre dans le fichier CSV correspondant à la catégorie
            for book in books:
                writer.writerow([book])
                

