import sorts
import utils

bookshelf = utils.load_books('bookshelf.csv')

def by_title_ascending(book_a, book_b):
  return book_a["title_lower"] > book_b["title_lower"]

def by_title_descending(book_a, book_b):
  return book_a["title_lower"] < book_b["title_lower"]

def by_author_ascending(book_a, book_b):
  return book_a["author_lower"] > book_b["author_lower"]

def by_author_descending(book_a, book_b):
  return book_a["author_lower"] < book_b["author_lower"]