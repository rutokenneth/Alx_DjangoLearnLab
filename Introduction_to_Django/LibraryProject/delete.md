### Delete Operation

**Command:**

```python
from library.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four") # Get the updated book
book.delete()
print(Book.objects.all()) # Try to retrieve all books to confirm deletion

Okay, I will continue by providing the content for `retrieve.md`, `update.md`, and `delete.md`, following the established format.

-----

### `retrieve.md`

````markdown
### Retrieve Operation

**Command:**

```python
from library.models import Book
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
````

**Output:**

```
# Expected output:
# Title: 1984, Author: George Orwell, Publication Year: 1949
```

````

---

### `update.md`

```markdown
### Update Operation

**Command:**

```python
from library.models import Book
book = Book.objects.get(title="1984") # Or by primary key if you have it: Book.objects.get(pk=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
````

**Output:**

```
# Expected output:
# Nineteen Eighty-Four
```

-----

### `delete.md`

````markdown
### Delete Operation

**Command:**

```python
from library.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four") # Get the updated book
book.delete()
print(Book.objects.all()) # Try to retrieve all books to confirm deletion
````

**Output:**

```
# Expected output:
# <QuerySet []>
# This indicates that there are no Book instances left in the database.
```
