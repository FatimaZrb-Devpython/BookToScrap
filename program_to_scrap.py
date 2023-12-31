from get_all_categories import *
from get_books_one_category import *
from get_one_book import *


url = 'https://books.toscrape.com/index.html'

# Récupérer toutes les catégories
categories = get_all_categories(url)
save_categories(categories)

# Parcourir chaque catégorie
for category in categories:
   # Récupérer les livres pour cette catégorie
    books = get_books_one_category(category)
     
    save_books_category(books, category)

    # Parcourir chaque livre de la catégorie actuelle
    for book in books:
        # Obtenir les détails du livre
        title,description,picture,category_book,upc,price_excl_tax,price_incl_tax,available,review= get_one_book(book)
        
        # Sauvegarder le livre dans le fichier correspondant à la catégorie
        save_book(title,description,picture,category_book,upc,price_excl_tax,price_incl_tax,available,review,category)
        get_picture(title,picture,category)


