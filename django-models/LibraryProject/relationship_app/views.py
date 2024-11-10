# Create your views here.
from django.shortcuts import render, redirect
from .models import Library
from django.views.generic.detail import DetailView
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

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
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Admin view, accessible only to Admin users
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
# Function to check if user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Librarian view, accessible only to Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
# Function to check if user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Member view, accessible only to Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')