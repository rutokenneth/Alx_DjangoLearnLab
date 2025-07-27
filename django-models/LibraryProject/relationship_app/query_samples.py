# relationship_app/query_data.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """
    Queries and prints all books by a specific author.
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\n--- Books by {author.name} ---")
        if books:
            for book in books:
                print(f"- {book.title}")
        else:
            print(f"No books found for {author_name}.")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_books_in_library(library_name):
    """
    Lists all books in a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\n--- Books in {library.name} Library ---")
        if books:
            for book in books:
                print(f"- {book.title} (by {book.author.name})")
        else:
            print(f"No books found in {library_name} Library.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def retrieve_librarian_for_library(library_name):
    """
    Retrieves and prints the librarian for a specific library.
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"\n--- Librarian for {library.name} Library ---")
        print(f"Librarian: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for '{library_name}' Library.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example Usage:

    # 1. Populate some sample data (optional, but good for testing)
    # You would typically do this through the Django admin or data migrations
    print("--- Populating Sample Data (if not already present) ---")
    author1, created = Author.objects.get_or_create(name="J.K. Rowling")
    if created: print(f"Created Author: {author1.name}")
    author2, created = Author.objects.get_or_create(name="George Orwell")
    if created: print(f"Created Author: {author2.name}")

    book1, created = Book.objects.get_or_create(title="Harry Potter and the Sorcerer's Stone", author=author1)
    if created: print(f"Created Book: {book1.title}")
    book2, created = Book.objects.get_or_create(title="1984", author=author2)
    if created: print(f"Created Book: {book2.title}")
    book3, created = Book.objects.get_or_create(title="Animal Farm", author=author2)
    if created: print(f"Created Book: {book3.title}")
    book4, created = Book.objects.get_or_create(title="Harry Potter and the Chamber of Secrets", author=author1)
    if created: print(f"Created Book: {book4.title}")

    library1, created = Library.objects.get_or_create(name="Central Library")
    if created:
        library1.books.add(book1, book2, book4)
        print(f"Created Library: {library1.name} and added books.")
    
    library2, created = Library.objects.get_or_create(name="Community Library")
    if created:
        library2.books.add(book3)
        print(f"Created Library: {library2.name} and added books.")

    librarian1, created = Librarian.objects.get_or_create(name="Alice Smith", library=library1)
    if created: print(f"Created Librarian: {librarian1.name} for {library1.name}")
    librarian2, created = Librarian.objects.get_or_create(name="Bob Johnson", library=library2)
    if created: print(f"Created Librarian: {librarian2.name} for {library2.name}")

    # --- Perform the queries ---
    query_books_by_author("J.K. Rowling")
    query_books_by_author("George Orwell")
    query_books_by_author("NonExistent Author")

    list_books_in_library("Central Library")
    list_books_in_library("Community Library")
    list_books_in_library("NonExistent Library")

    retrieve_librarian_for_library("Central Library")
    retrieve_librarian_for_library("Community Library")
    retrieve_librarian_for_library("Library Without Librarian") # This will demonstrate error handling
    retrieve_librarian_for_library("NonExistent Library")
