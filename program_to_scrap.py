from get_all_categories import *
from get_books_one_category import *
from get_one_book import *


url = 'https://books.toscrape.com/index.html'

# Récupérer toutes les catégories
categories = get_all_categories(url)
# save_categories(categories)

# # Parcourir chaque catégorie
for category in categories:
#     # Récupérer les livres pour cette catégorie
    books = get_books_one_category(category)
    # save_books_category(books, category)

# #     # Parcourir chaque livre de la catégorie actuelle
    for book in books:
# category = 'https://books.toscrape.com/catalogue/category/books/poetry_23/index.html'
# book =  'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

        # Obtenir les détails du livre
        title, description, picture, upc, category_book, price_excl_tax, price_incl_tax, available, review = get_one_book(book)

        # Sauvegarder le livre dans le fichier correspondant à la catégorie
        save_book(title, description, picture, upc, category_book, price_excl_tax, price_incl_tax, available, review,categories)
            # get_picture(title,picture)


