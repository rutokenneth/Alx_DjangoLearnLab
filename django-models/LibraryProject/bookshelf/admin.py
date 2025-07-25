from django.contrib import admin
from .models import Book
# Register your models here.
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    # 1. Display specific fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # 2. Add list filters
    list_filter = ('publication_year', 'author') # You can filter by publication year and author

    # 3. Add search capabilities
    search_fields = ('title', 'author') # Allows searching by title and author
