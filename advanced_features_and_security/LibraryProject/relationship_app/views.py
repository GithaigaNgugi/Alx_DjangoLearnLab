# Create your views here.
from django.shortcuts import render, redirect
from .models import Library
from django.views.generic.detail import DetailView
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book
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

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome to the Admin dashboard!")
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian dashboard!")
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome to the Member dashboard!")



@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        if title and author_id:
            Book.objects.create(title=title, author_id=author_id)
            return redirect('book_list')
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.author_id = request.POST.get('author_id', book.author_id)
        book.save()
        return redirect('book_list')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})