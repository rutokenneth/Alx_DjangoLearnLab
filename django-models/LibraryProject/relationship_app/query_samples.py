# relationship_app/query_samples.py

import os
import django

# Set up Django environment
# This is crucial for running Django ORM queries outside of the manage.py shell
# or a Django view. It tells Django where to find your project's settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Import the models we defined in relationship_app/models.py
from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    """
    This function demonstrates various Django ORM queries based on the defined relationships.
    It first ensures some sample data exists, then performs the queries.
    """
    print("--- Ensuring Sample Data Exists ---")
    # Create sample data if it doesn't already exist
    # This makes the script runnable independently for demonstration
    try:
        author1, created = Author.objects.get_or_create(name="Jane Austen")
        if created:
            print(f"Created Author: {author1.name}")

        author2, created = Author.objects.get_or_create(name="George Orwell")
        if created:
            print(f"Created Author: {author2.name}")

        book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author1)
        if created:
            print(f"Created Book: {book1.title}")

        book2, created = Book.objects.get_or_create(title="1984", author=author2)
        if created:
            print(f"Created Book: {book2.title}")

        book3, created = Book.objects.get_or_create(title="Sense and Sensibility", author=author1)
        if created:
            print(f"Created Book: {book3.title}")

        book4, created = Book.objects.get_or_create(title="Animal Farm", author=author2)
        if created:
            print(f"Created Book: {book4.title}")

        library1, created = Library.objects.get_or_create(name="City Central Library")
        if created:
            print(f"Created Library: {library1.name}")
            # Add books to the library (Many-to-Many relationship)
            library1.books.add(book1, book2, book3)
            print(f"Added books to {library1.name}")

        library2, created = Library.objects.get_or_create(name="University Archives")
        if created:
            print(f"Created Library: {library2.name}")
            library2.books.add(book2, book4)
            print(f"Added books to {library2.name}")

        librarian1, created = Librarian.objects.get_or_create(name="Alice Smith", library=library1)
        if created:
            print(f"Created Librarian: {librarian1.name}")

        librarian2, created = Librarian.objects.get_or_create(name="Bob Johnson", library=library2)
        if created:
            print(f"Created Librarian: {librarian2.name}")

    except Exception as e:
        print(f"Error creating sample data: {e}")
        print("Please ensure you have run 'python manage.py makemigrations relationship_app' and 'python manage.py migrate'")
        return # Exit if data creation fails

    print("\n--- Performing Queries ---")

    # 1. Query all books by a specific author
    print("\n--- Query 1: Books by Jane Austen ---")
    try:
        # Get the author object first
        jane_austen = Author.objects.get(name="Jane Austen")
        # Use the related_name 'books' defined in the Book model's ForeignKey
        jane_austen_books = jane_austen.books.all()
        if jane_austen_books.exists():
            print(f"Books by {jane_austen.name}:")
            for book in jane_austen_books:
                print(f"- {book.title}")
        else:
            print(f"No books found for {jane_austen.name}.")
    except Author.DoesNotExist:
        print("Author 'Jane Austen' not found.")
    except Exception as e:
        print(f"Error querying books by author: {e}")


    # 2. List all books in a library
    print("\n--- Query 2: Books in City Central Library ---")
    try:
        # Get the library object
        city_library = Library.objects.get(name="City Central Library")
        # Access the ManyToMany related manager 'books'
        library_books = city_library.books.all()
        if library_books.exists():
            print(f"Books in {city_library.name}:")
            for book in library_books:
                print(f"- {book.title} (by {book.author.name})")
        else:
            print(f"No books found in {city_library.name}.")
    except Library.DoesNotExist:
        print("Library 'City Central Library' not found.")
    except Exception as e:
        print(f"Error querying books in library: {e}")


    # 3. Retrieve the librarian for a library
    print("\n--- Query 3: Librarian for University Archives ---")
    try:
        # Get the library object
        university_library = Library.objects.get(name="University Archives")
        # Access the OneToOne related manager 'librarian'
        # The related_name 'librarian' was defined on the OneToOneField in Librarian model
        librarian = university_library.librarian
        print(f"Librarian for {university_library.name}: {librarian.name}")
    except Library.DoesNotExist:
        print("Library 'University Archives' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for 'University Archives'.")
    except Exception as e:
        print(f"Error querying librarian for library: {e}")


if __name__ == '__main__':
    run_queries()
