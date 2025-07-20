from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the author.")
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="The title of the book.")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', help_text="The author of the book.")
    def __str__(self):
        return f"{self.title} by {self.author.name}"

class Library(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the library.")
    books = models.ManyToManyField(Book, related_name='libraries', help_text="The books available in this library.")
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the librarian.")
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian', help_text="The library this librarian manages.")

    def __str__(self):
        return f"{self.name} (Librarian at {self.library.name})"
