import csv

# Loads data from the bookshelf
def load_books(filename):
  bookshelf = []
  with open(filename) as file:
      shelf = csv.DictReader(file)
      for book in shelf:
          # Transforms to lowercase and appends item to the list
          book['author_lower'] = book["author"].lower()
          book["title_lower"] = book["title"].lower()
          bookshelf.append(book)
  return bookshelf