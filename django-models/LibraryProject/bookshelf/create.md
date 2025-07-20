### Create Operation

**Command:**

```python
from library.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# The 'book' object will be an instance of the Book model, representing the newly created record in the database.
# For example, printing 'book' might show something like:
# <Book: 1984>
