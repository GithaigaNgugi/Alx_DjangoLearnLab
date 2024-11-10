from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library
# Create your views here.
from django.shortcuts import render
from .models import Book

# Function-based view to list all books and their authors
def book_list(request):
    # Retrieve all books from the database
    books = Book.objects.all()

    # Pass the books to the template for rendering
    return render(request, 'relationship_app/book_list.html', {'books': books})


# Class-based view to display details of a specific library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Specify the template
    context_object_name = 'library'  # Name to reference the object in the template
