from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library, Author, Librarian

# Create your views here.
def book_list(request):
    books = Book.objects.all().order_by('title')
    
    output = []
    output.append("<h1>All Books<h2>")
    output.append("<ul>")
    for book in books:
        output.append(f"<li>{book.title} (Author: {book.author.name})</li>")
    output.append("<ul>")
    return HttpResponse("".join(output))

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books_in_library']=library.books.all().order_by('title')
        try:
            context['librarian'] = library.librarian # Access the related librarian directly
        except Librarian.DoesNotExist:
            context['librarian'] = None # No librarian found for this library

        return context
