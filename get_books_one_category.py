import requests
from bs4 import BeautifulSoup
# import csv

def get_books_one_category (url):
    
    url_split = url.split('/')
    url_split_bis= url_split[0:len(url_split)-1]
    path = '/'.join(url_split_bis)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    books = []

    row = soup.find("ol", class_='row').find_all('h3')
    for a in row :
        a =  a.find('a')
        link = a.get('href')
        link = link.replace('../../../','')
        books.append( path + '/' + link)
        
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
                books.append('https://books.toscrape.com/catalogue' + link)
                
            next = soup.find('ul', class_= 'pager').find('li', class_='next')
    except: 
        return books
    
    return books



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
        
