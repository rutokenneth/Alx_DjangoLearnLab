from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .models import Book, Library, Author, Librarian
from django.urls import reverse_lazy
# from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import permission_required

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
        # try:
        #     context['librarian'] = library.librarian # Access the related librarian directly
        # except Librarian.DoesNotExist:
        #     context['librarian'] = None # No librarian found for this library

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

# role checker helper functions
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Role-Based Views ---
@login_required
@user_passes_test(is_librarian, login_url='/relationship_app/templates/registration/login.html')
def librarian_view(request):
    """View accessible only by Librarian users."""
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/accounts/login/')
def member_view(request):
    """View accessible only by Member users."""
    return render(request, 'relationship_app/member_view.html')

@login_required # Ensures user is logged in
@user_passes_test(is_admin, login_url='/accounts/login/') # Redirects to login if not admin
def admin_view(request):
    """View accessible only by Admin users."""
    return render(request, 'relationship_app/admin_view.html')

# new views with custom permissions
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_name = request.POST.get('author')
        author, created = Author.objects.get_or_create(name=author_name)
        Book.objects.create(title=title, author=author)
        return render(request, 'relationship_app/books.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_name = request.POST.get('author')
        author, created = Author.objects.get_or_create(name=author_name)
        book.author = author
        book.save()
        return redirect('book_list')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    """View to delete a book, restricted to users with 'can_delete_book' permission."""
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_confirm.html', {'book': book})
