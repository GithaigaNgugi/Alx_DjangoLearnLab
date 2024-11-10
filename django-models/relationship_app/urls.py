from django.urls import path
from . import views
from .views import list_books
from .views import LibraryDetailView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
]
