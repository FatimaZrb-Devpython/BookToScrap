from get_all_categories import *
from get_books_one_category import *
from get_one_book import *


url = 'https://books.toscrape.com/index.html'
    
categories = get_all_categories (url)
        
   
for category in categories:
    books = get_books_one_category (category)

for book in books:
    one_book = get_one_book(book)
    


