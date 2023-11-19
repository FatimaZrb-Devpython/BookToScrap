import requests
from bs4 import BeautifulSoup
# import csv




def get_one_book(link) : 
    
    link = 'https://books.toscrape.com/catalogue/david-and-goliath-underdogs-misfits-and-the-art-of-battling-giants_146/index.html'
    
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
    src = img.get('src')
    image.append(src.strip())

    
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

# # Créer un nouveau fichier pour écrire dans le fichier appelé « book.csv »
# with open('book.csv', 'w') as csv_file:
#         # Créer un objet writer (écriture) avec ce fichier
#     writer = csv.writer(csv_file, delimiter=',')
#     writer.writerow(en_tete)
#         # Parcourir les éléments- zip permet d'itérer sur deux tdes ou plus à la fois
#     for title,description,upc,price_excl_tax,price_incl_tax,available,review,url in zip(collect()):
#             # Créer une nouvelle ligne pour chaque éléments à ce moment de la boucle
#         ligne = [title,description,upc,price_excl_tax,price_incl_tax,available,review,url] 
#         writer.writerow(ligne)

