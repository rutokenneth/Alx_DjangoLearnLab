(InteractiveConsole)
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> print(book)
1984 by George Orwell
>>> book = Book.objects.get(title="1984")
>>> print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
Title: 1984, Author: George Orwell, Publication Year: 1949
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.title)
Nineteen Eighty-Four
