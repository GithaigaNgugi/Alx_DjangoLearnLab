# Create your views here.
from django.shortcuts import render, redirect
from .models import Library
from django.views.generic.detail import DetailView
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
# Function-based view to list all books and their authors
def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()

    # Pass the books to the template for rendering
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to display details of a specific library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Specify the template
    context_object_name = 'library'  # Name to reference the object in the template

# User registration view
def custom_logout(request):
    logout(request)  # Logs out the user
    return render(request, 'relationship_app/logout.html')  # Renders custom template

# Custom login view to render login.html
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the desired page after login
        else:
            return render(request, 'relationship_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'relationship_app/login.html')  # Render the login form

# Registration view to render register.html and handle user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user right after registration
            return redirect('home')  # Redirect to a desired page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})