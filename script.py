import sorts
import utils

bookshelf = utils.load_books('bookshelf.csv')

# Sorts bookshelf by title A-Z
def by_title_ascending(book_a, book_b):
  return book_a["title_lower"] > book_b["title_lower"]

# Sorts bookshelf by title Z-A
def by_title_descending(book_a, book_b):
  return book_a["title_lower"] < book_b["title_lower"]

# Sorts bookshelf by author A-Z
def by_author_ascending(book_a, book_b):
  return book_a["author_lower"] > book_b["author_lower"]

# Sorts bookshelf by author Z-A
def by_author_descending(book_a, book_b):
  return book_a["author_lower"] < book_b["author_lower"]