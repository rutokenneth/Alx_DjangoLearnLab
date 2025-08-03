from django.urls import path
from . import views
from .views import LibraryDetailView, register, admin_view, librarian_view, member_view, add_book, edit_book, delete_book
urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), # New URL pattern
    #user accounts paths 
    path('accounts/register/', views.register, name='register'),
    
    # New Role-Based URLs
    path('admin-dashboard/', admin_view, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_view, name='librarian_dashboard'),
    path('member-dashboard/', member_view, name='member_dashboard'),
    
    # permission required URLs
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]
