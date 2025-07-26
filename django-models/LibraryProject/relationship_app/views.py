from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import Book, Library

def book_list(request):
    books = Books.objects.all().order_by('title')
    context = {
        'books':books,
    }
    return render(request, 'relationship_app/book_list.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
