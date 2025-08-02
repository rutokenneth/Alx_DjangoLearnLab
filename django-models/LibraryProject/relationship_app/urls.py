from django.urls import path
from . import views
from .views import LibraryDetailView
urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), # New URL pattern
    #user accounts paths 
    path('accounts/register/', views.register, name='register'),
    # path('profile/', views.profile_view, name='profile'),
    # path('admin-dashboard/', admin_view, name='admin_dashboard'),
    # path('librarian-dashboard/', librarian_view, name='librarian_dashboard'),
    # path('member-dashboard/', member_view, name='member_dashboard'),
]
