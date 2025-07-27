from django.urls import path
from . import views
from .views import LibraryDetailView
urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), # New URL pattern
]
