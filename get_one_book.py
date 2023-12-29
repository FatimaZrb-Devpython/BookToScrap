import requests
from bs4 import BeautifulSoup
import csv
import os
import re
import urllib.request


def get_one_book(book):
    book = book.replace("../../", "")
    page = requests.get(book, timeout=(10, 30))
    soup = BeautifulSoup(page.content, "html.parser")

    # Extraction du titre dans le DOM
    title = soup.find("h1").string

    # Extraction de toutes les balises p dans le DOM afin d'obtenir la balise p arrivant en 3eme position pour récupérer la description

    paragraph = soup.find_all("p")
    description = paragraph[3]
    description = description.string

    # Extraction de l'url de l'image du livre
    images = soup.find("div", id="product_gallery")
    img = images.find("img")
    item = img.get("src")
    item = item.replace("../../", "")
    picture = "https://books.toscrape.com/" + item

    ul = soup.find("ul", class_="breadcrumb").findAll(
        "li")  
    # De quel catégorie est le produit
    li = ul[2]
    category_book = li.a.get_text()
    category_book = category_book

    # Extraction de la balise table afin de récupérer les balises td qui correspondent à chaque éléments nécessaire

    table = soup.find("table", class_="table table-striped")
    tds = table.find_all("td")

    upc = tds[0]  # Code UPC du livre
    upc = upc.string

    price_excl_tax = tds[2]  # Prix hors taxe du livre
    price_excl_tax = price_excl_tax.string

    price_incl_tax = tds[3]  # Prix avec taxe du livre
    price_incl_tax = price_incl_tax.string

    available = tds[5]  # Quantité restant du livre
    available = available.string

    review = tds[6]  # Nombre d'étoile du livre
    review = review.string

    return (
        title,
        description,
        picture,
        category_book,
        upc,
        price_excl_tax,
        price_incl_tax,
        available,
        review,
    )


def save_book(
    title,
    description,
    picture,
    category_book,
    upc,
    price_excl_tax,
    price_incl_tax,
    available,
    review,
    category,
):
    try:
        # Recherche de la catégorie dans la liste complète des catégories
        category = re.sub(r"[_0-9]", "", category[0])
        category = category.replace("-", " ")

        category_title = category

        new_title = re.sub(r"[^\w\s]", "", title)

        # Raccourcir le titre s'il est trop long
        if len(new_title) > 70:
            # Raccourcir le titre et ajouter "..."
            new_title = new_title[:67] + "..."

        file_path = rf"./categories/{category_title}/{new_title}.csv"

        # Vérifier si le fichier existe déjà
        file_exists = os.path.isfile(file_path)

        # Créer un nouveau fichier pour écrire dans le fichierc
        with open(file_path, "w", newline="", encoding="utf-8") as csv_file:
            # Créer un objet writer (écriture) avec ce fichier
            writer = csv.writer(csv_file, delimiter=",")

            # Si le fichier n'existe pas, écrire les en-têtes
            if not file_exists:
                en_tete = [
                    "title",
                    "description",
                    "picture",
                    "category_book",
                    "upc",
                    "price_excl_tax",
                    "price_incl_tax",
                    "available",
                    "review",
                ]
                writer.writerow(en_tete)

            # Créer une nouvelle ligne pour chaque élément
            ligne = [
                title,
                description,
                picture,
                category_book,
                upc,
                price_excl_tax,
                price_incl_tax,
                available,
                review,
            ]
            writer.writerow(ligne)

    except Exception as error:
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"An error occurred: {type(error).__name__}\n")
            print("error save", error)


def get_picture(title, picture, category):
    try:
        title_category = category[0]
        title_category = re.sub(r"[_0-9]", "", title_category)
        category = title_category.replace("-", " ")

        new_title = re.sub(r"[^\w\s]", "", title)

        # Raccourcir le titre s'il est trop long
        if len(new_title) > 70:
            # Raccourcir le titre et ajouter "..."
            new_title = new_title[:67] + "..."

        file_path = rf"./categories/{category}/{new_title}.jpg"

        # Vérifier si le fichier existe déjà
        file_exists = os.path.isfile(file_path)

        # Ouvre l'URL de l'image et lit son contenu
        with urllib.request.urlopen(picture) as url:
            picture = url.read()

        if not file_exists:
            # Enregistre le contenu de l'image dans un fichier
            with open(file_path, "wb") as file:
                file.write(picture)

    except Exception as error:
        with open("error_log.txt", "a") as log_file:
            log_file.write(f"An error occurred: {type(error).__name__}\n")
            print("error picture", error)
