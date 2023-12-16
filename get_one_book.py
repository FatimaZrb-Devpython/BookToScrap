import requests
from bs4 import BeautifulSoup
import csv
import os
# import urllib.request

def get_one_book(book) : 
    
    book = book.replace('../../','')
    page = requests.get(book, timeout=(10, 30))
    soup = BeautifulSoup(page.content, 'html.parser')

# Extraction du titre dans le DOM
    title = soup.find("h1").string

#Extraction de toutes les balises p dans le DOM afin d'obtenir la balise p arrivant en 3eme position pour récupérer la description

    paragraph = soup.find_all('p')
    description = paragraph[3]
    description = ('description : ',description.string)


#Extraction de l'url de l'image du livre
    images = soup.find("div", id='product_gallery')
    img = images.find("img")
    item = img.get('src')
    item = item.replace('../../','')
    picture  = ('https://books.toscrape.com/' + item)
    
    ul = soup.find("ul", class_='breadcrumb').findAll("li")   # De quel catégorie est le produit
    li= ul[2]
    category_book = li.a.get_text()
    category_book = ('category',category_book)
    
# Extraction de la balise table afin de récupérer les balises td qui correspondent à chaque éléments nécessaire

    table = soup.find("table",class_='table table-striped')
    tds = table.find_all('td')

    
    upc = tds[0]# Code UPC du livre 
    upc = ('upc : ',upc.string)
            
            
    price_excl_tax = tds[2] # Prix hors taxe du livre 
    price_excl_tax = ('price_excl_tax',price_excl_tax.string)
            
    price_incl_tax = tds[3] # Prix avec taxe du livre
    price_incl_tax = ('price_incl_tax',price_incl_tax.string)
            
    available = tds[5] # Quantité restant du livre
    available = ('available',available.string)
            
    review = tds[6] # Nombre d'étoile du livre
    review = ('review',review.string)
    

    return title,description,picture,upc,category_book,price_excl_tax,price_incl_tax,available,review
    
          
      

def save_book(title, description, picture, upc, category_book, price_excl_tax, price_incl_tax, available, review, categories):
    
    try:
        # Recherche de la catégorie dans la liste complète des catégories
        matching_categories = [category for category in categories if category[1] == category_book]
        print(matching_categories)
        if matching_categories:
            # Extraire le titre de la catégorie
            category_title = matching_categories[0][1]
            print(category_title)
            # Créer un nouveau fichier pour écrire dans le dossier de la catégorie
            title = title.replace(" ", "_") + '.csv'
            file_path = fr'C:\Users\fatim\OneDrive\Bureau\formation 1\Projet_2_Books_Online/categories/{category_title}/{title}'


            # Vérifier si le fichier existe déjà
            file_exists = os.path.isfile(file_path)

            # Créer un nouveau fichier pour écrire dans le fichier
            with open(file_path + '.csv', 'a', newline='') as csv_file:
                # Créer un objet writer (écriture) avec ce fichier
                writer = csv.writer(csv_file, delimiter=',')

                # Si le fichier n'existe pas, écrire les en-têtes
                if not file_exists:
                    en_tete = ["title", "description", "picture", "upc", "category_book", "price_excl_tax", "price_incl_tax", "available", "review"]
                    writer.writerow(en_tete)

                # Créer une nouvelle ligne pour chaque élément
                ligne = [title, description, picture, upc, category_book, price_excl_tax, price_incl_tax, available, review]
                writer.writerow(ligne)
                
    except Exception as error:
        print("An error occurred while saving book:", type(error).__name__)


# # def get_picture (title,picture):
# #     print(title,picture)
    
# #     # Ouvre l'URL de l'image et lit son contenu
# #     with urllib.request.urlopen(picture) as url:
# #             picture_content = url.read()

# #             # Enregistre le contenu de l'image dans un fichier
# #             with open(f"{title}.jpg", "wb") as file:
# #                 picture_url= csv.write(picture_content)
# #                 file.writer(picture_url)


        
            