import os
import django

# Set up the Django environment to use the project's settings
# Replace 'your_project_name' with the actual name of your Django project folder
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Import your models AFTER setting up Django
# Replace 'your_app_name' with the name of the app where your models are defined
from relationship_app.models import Author, Book, Library, Librarian

def populate_data():
    """
    Populates the database with some sample data for testing queries.
    Clears existing data to avoid duplicates on re-runs.
    """
    print("--- Clearing old data... ---")
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    print("--- Populating database with sample data... ---")

    # Create Authors
    author1 = Author.objects.create(name="J.R.R. Tolkien")
    author2 = Author.objects.create(name="George Orwell")
    author3 = Author.objects.create(name="Jane Austen")

    # Create Books
    book1 = Book.objects.create(title="The Hobbit", author=author1)
    book2 = Book.objects.create(title="The Lord of the Rings", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)
    book5 = Book.objects.create(title="Pride and Prejudice", author=author3)

    # Create Libraries and Librarians
    library1 = Library.objects.create(name="Central City Library")
    Librarian.objects.create(name="Mr. Anderson", library=library1)

    library2 = Library.objects.create(name="Northside Community Library")
    Librarian.objects.create(name="Ms. Evelyn Reed", library=library2)

    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book3, book5)
    library2.books.add(book2, book3, book4) # Note: '1984' is in both libraries

    print("--- Data population complete. ---\n")


def run_queries():
    """
    Executes the required queries and prints the results.
    """
    print("--- Running Queries ---")

    # 1. Query all books by a specific author (George Orwell)
    print("\n[1] Querying all books by 'George Orwell':")
    try:
        # First, get the author object
        george_orwell = Author.objects.get(name="George Orwell")
        # Then, use the reverse relationship to find all his books
        orwell_books = Book.objects.filter(author=george_orwell)
        if orwell_books:
            for book in orwell_books:
                print(f"  - {book.title}")
        else:
            print("  - No books found for this author.")
    except Author.DoesNotExist:
        print("  - Author 'George Orwell' not found in the database.")


    # 2. List all books in a specific library (Central City Library)
    print("\n[2] Listing all books in 'Central City Library':")
    try:
        # Get the library object
        central_library = Library.objects.get(name="Central City Library")
        # Access the ManyToManyField directly to get all related books
        library_books = central_library.books.all()
        if library_books:
            for book in library_books:
                print(f"  - {book.title} (by {book.author.name})")
        else:
            print("  - This library has no books.")
    except Library.DoesNotExist:
        print("  - Library 'Central City Library' not found.")


    # 3. Retrieve the librarian for a specific library (Northside Community Library)
    print("\n[3] Retrieving the librarian for 'Northside Community Library':")
    try:
        # Get the library object
        northside_library = Library.objects.get(name="Northside Community Library")
        # Access the OneToOneField reverse relationship
        # The related name is automatically 'librarian' (the model name in lowercase)
        librarian = northside_library.librarian
        print(f"  - The librarian is: {librarian.name}")
    except Library.DoesNotExist:
        print("  - Library 'Northside Community Library' not found.")
    except Librarian.DoesNotExist:
        # This happens if a Library exists but has no associated Librarian
        print("  - This library does not have an assigned librarian.")

    print("\n--- Queries Finished ---")


if __name__ == "__main__":
    # Populate data first to ensure queries have something to find
    populate_data()
    # Run the queries
    run_queries()
