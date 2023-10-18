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

# Creates a copy of the bookshelf in which the sorting will happen
bookshelf_copy = bookshelf.copy()

# Sorts the list in random order
#shuffle = sorts.shuffle(bookshelf_copy)

# Sorts by title A-Z using bubble sort algorithm
#bubble_sort_by_title_a_z = sorts.bubble_sort(bookshelf_copy, by_title_ascending)
# Sorts by title A-Z using quicksort algorithm
quicksort_by_title_a_z = sorts.quicksort(bookshelf_copy, 0, len(bookshelf_copy) - 1, by_title_ascending)

# Sorts by title Z-A using bubble sort algorithm
#bubble_sort_by_title_z_a = sorts.bubble_sort(bookshelf_copy, by_title_descending)
# Sorts by title Z-A using quicksort algorithm
#quicksort_by_title_z_a = sorts.quicksort(bookshelf_copy, 0, len(bookshelf_copy) - 1, by_title_descending)

# Sorts by author A-Z using bubble sort algorithm
#bubble_sort_by_author_a_z = sorts.bubble_sort(bookshelf_copy, by_author_ascending)
# Sorts by author A-Z using quicksort algorithm
#quicksort_by_author_a_z = sorts.quicksort(bookshelf_copy, 0, len(bookshelf_copy) - 1, by_author_ascending)

# Sorts by author Z-A using bubble sort algorithm
#bubble_sort_by_author_z_a = sorts.bubble_sort(bookshelf_copy, by_author_descending)
# Sorts by author Z-A using quicksort algorithm
#quicksort_by_author_z_a = sorts.quicksort(bookshelf_copy, 0, len(bookshelf_copy) - 1, by_author_descending)

# Displays the sorted list
for book in bookshelf_copy:
    print(book["title"] + ", " + book["author"])