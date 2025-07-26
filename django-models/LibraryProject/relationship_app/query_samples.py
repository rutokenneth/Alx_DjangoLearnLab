from relationship_app.models import Author, Book, Library, Librarian

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# relationship_app/query_examples.py

def query_books_by_specific_author(author_name):
    """
    Queries and lists all books written by a specific author.
    Demonstrates ForeignKey relationship query (Author -> Book).
    """
    print(f"\n--- Querying books by author: {author_name} ---")
    try:
        author = Author.objects.get(name=author_name)
        # Accessing related books using the 'related_name' defined in the Book model
        books = author.books.all()
        if books.exists():
            print(f"Books by {author.name}:")
            for book in books:
                print(f"  - {book.title}")
        else:
            print(f"No books found for {author.name}.")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def list_all_books_in_library(library_name):
    """
    Lists all books available in a specific library.
    Demonstrates ManyToManyField relationship query (Library -> Book).
    """
    print(f"\n--- Listing books in library: {library_name} ---")
    try:
        library = Library.objects.get(name=library_name)
        # Accessing related books through the ManyToManyField
        books = library.books.all()
        if books.exists():
            print(f"Books in {library.name}:")
            for book in books:
                print(f"  - {book.title} (by {book.author.name})")
        else:
            print(f"No books found in {library.name}.")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def retrieve_librarian_for_library(library_name):
    """
    Retrieves and displays the librarian for a specific library.
    Demonstrates OneToOneField relationship query (Library -> Librarian).
    """
    print(f"\n--- Retrieving librarian for library: {library_name} ---")
    try:
        library = Library.objects.get(name=library_name)
        # Accessing the related librarian using the 'related_name' defined in the Librarian model
        librarian = library.librarian
        print(f"The librarian for '{library.name}' is: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist: # This can happen if a library exists but no librarian is assigned
        print(f"No librarian found for '{library_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # --- IMPORTANT ---
    # Before running this script:
    # 1. Make sure you have run `python manage.py makemigrations relationship_app`
    #    and `python manage.py migrate` to create the database tables.
    # 2. Populate your database with some sample data using the Django admin
    #    (create a superuser with `python manage.py createsuperuser` and access /admin)
    #    or via the Django shell (`python manage.py shell`).
    #
    # Example data you might create:
    # Authors: J.K. Rowling, Stephen King
    # Books: "Harry Potter and the Sorcerer's Stone" (by J.K. Rowling), "The Shining" (by Stephen King), "It" (by Stephen King)
    # Libraries: Central Library, Community Library
    # Link books to libraries: Central Library has Harry Potter, The Shining. Community Library has It.
    # Librarians: Alice (for Central Library), Bob (for Community Library)

    # Replace 'your_project_name' in os.environ.setdefault above with your actual project name.
    # For example, if your outer project folder is 'myproject' and the inner settings folder is also 'myproject',
    # it would be 'myproject.settings'.

    print("--- Running Django Relationship Query Examples ---")

    # Example Queries (adjust names based on your sample data)
    query_books_by_specific_author("J.K. Rowling")
    query_books_by_specific_author("Stephen King")
    query_books_by_specific_author("NonExistent Author")

    list_all_books_in_library("Central Library")
    list_all_books_in_library("Community Library")
    list_all_books_in_library("NonExistent Library")

    retrieve_librarian_for_library("Central Library")
    retrieve_librarian_for_library("Community Library")
    retrieve_librarian_for_library("NonExistent Library")

    print("\n--- End of Query Examples ---")
