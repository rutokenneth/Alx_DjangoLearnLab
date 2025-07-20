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

# Expected output:
# Nineteen Eighty-Four
