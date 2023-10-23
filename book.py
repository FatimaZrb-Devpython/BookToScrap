import requests
from bs4 import BeautifulSoup
# import csv




def collect(url) : 
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    titles = soup.find("h1")
    title = []
    title.append(titles.string)
    
    ps = soup.find_all('p')
    p = []
    for p in ps : 
        description = ps[3]
        p.append(description.string)

    images = soup.find("div", id='product_gallery')
    image = [] 
    for image in images : 
        img = image.find("img")
        url = img['src']
        image.append(url.string)

    tds = soup.find_all('td')
    td = []
    for td in tds : 
            upc = tds[0]
            td.append(upc.string)
            
            price_excl_tax=tds[2]
            td.append(price_excl_tax)
            
            price_incl_tax=tds[3]
            td.append(price_incl_tax.string)
            
            available=tds[5]
            td.append(available.string)
            
            category=tds[1]
            td.append(category.string)
            
            review=tds[6]
            td.append(review.string)
        
            # return title,description,upc,price_excl_tax,price_incl_tax,available,review,url

title,description,upc,price_excl_tax,price_incl_tax,available,review,url,image = collect("http://books.toscrape.com/catalogue/shakespeares-sonnets_989/index.html")

# def write () :
# # Créer une liste pour les en-têtes
#     en_tete = ["title","description","upc","price_excl_tax","price_incl_tax","available","review","url"]

# # Créer un nouveau fichier pour écrire dans le fichier appelé « book.csv »
#     with open('book.csv', 'w') as csv_file:
#         # Créer un objet writer (écriture) avec ce fichier
#         writer = csv.writer(csv_file, delimiter=',')
#         writer.writerow(en_tete)
#         # Parcourir les éléments- zip permet d'itérer sur deux listes ou plus à la fois
#         for title,description,upc,price_excl_tax,price_incl_tax,available,review,url in zip(collect()):
#             # Créer une nouvelle ligne pour chaque éléments à ce moment de la boucle
#             ligne = [title,description,upc,price_excl_tax,price_incl_tax,available,review,url] 
#             writer.writerow(ligne)

# write()
