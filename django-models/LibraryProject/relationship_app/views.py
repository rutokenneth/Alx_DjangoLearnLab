from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import Book, Library, Author, Librarian


# Create your views here.
def book_list(request):
    books = Book.objects.all().order_by('title')
    
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

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

# registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login') # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required # Decorator to restrict access to authenticated users
def profile_view(request):
    """
    A simple example view that requires the user to be logged in.
    """
    return render(request, 'profile.html', {'user': request.user})
