import requests
from bs4 import BeautifulSoup
# import csv


def get_one_book(link) : 
    
    link_split = link.split('/')
    link_before= link_split[0:len(link_split)-5]
    link_title = link_split[7:len(link_split)]
    link = '/'.join(link_before + link_title)
    
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')

#Extraction du titre dans le DOM
    titles = soup.find("h1")
    title = []
    title.append(titles.string)

#Extraction de toutes les balises p dans le DOM afin d'obtenir la balise p arrivant en 3eme position pour récupérer la description
   
    descriptions = soup.find_all('p')[3]
    description = []
    description.append(descriptions.string)

#Extraction de l'url de l'image du livre
    images = soup.find("div", id='product_gallery')
    image = []
    img = images.find("img")
    item = img.get('src')
    item = item.replace('../../','')
    picture  = ('https://books.toscrape.com/' + item)
    image.append(picture.strip())

    
# Extraction de la balise table afin de récupérer les balises td qui correspondent à chaque éléments nécessaire

    table = soup.find("table",class_='table table-striped')
    tds = table.find_all('td')

    list = []
    
    upc = tds[0]# Code UPC du livre 
    list.append(('upc',upc.text))
            
    category = tds[1]  # De quel catégorie est le produit
    list.append(('category',category.text))
            
    price_excl_tax = tds[2] # Prix hors taxe du livre 
    list.append(('price_excl_tax',price_excl_tax.text))
            
    price_incl_tax = tds[3] # Prix avec taxe du livre
    list.append(('price_incl_tax',price_incl_tax.text))
            
    available = tds[5] # Quantité restant du livre
    list.append(('available',available.text))
            
    review = tds[6] # Nombre d'étoile du livre
    list.append(('review',review.text))
    
    return title,description,image,upc,category,price_excl_tax,price_incl_tax,available,review
            

 
# Créer une tde pour les en-têtes
# en_tete = ["title","description","upc","price_excl_tax","price_incl_tax","available","review","url"]
# collect = get_one_book()
# title,description,image,upc,price_excl_tax,price_incl_tax,available,review = collect
# # Créer un nouveau fichier pour écrire dans le fichier appelé « one_book.csv »
# with open('one_book.csv', 'w') as csv_file:
#     # Créer un objet writer (écriture) avec ce fichier
#     writer = csv.writer(csv_file, delimiter=',')
#     writer.writerow(en_tete)
#     # Parcourir les éléments- zip permet d'itérer sur deux tdes ou plus à la fois
#     for title,description,image,upc,price_excl_tax,price_incl_tax,available,review in zip(collect):
#         # Créer une nouvelle ligne pour chaque éléments à ce moment de la boucle
#         ligne = [title,description,image,upc,price_excl_tax,price_incl_tax,available,review] 
#         writer.writerow(ligne)

