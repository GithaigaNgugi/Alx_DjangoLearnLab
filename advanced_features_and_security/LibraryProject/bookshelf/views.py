from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm

# View to list all books
@permission_required('app_name.can_view', raise_exception=True)
def book_list(request):
    """
    Lists all books. Requires 'can_view' permission.
    """
    books = Book.objects.all()  # Secure use of Django ORM
    return render(request, 'books/book_list.html', {'books': books})


# View to create a new book
@permission_required('app_name.can_create', raise_exception=True)
def book_create(request):
    """
    Handles book creation. Requires 'can_create' permission.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)  # Use Django forms for validation
        if form.is_valid():
            form.save()  # Save the validated data to the database
            return redirect('book_list')  # Redirect to the book list view
    else:
        form = BookForm()
    return render(request, 'books/book_create.html', {'form': form})


# View to edit an existing book
@permission_required('app_name.can_edit', raise_exception=True)
def book_edit(request, pk):
    """
    Handles book editing. Requires 'can_edit' permission.
    """
    book = get_object_or_404(Book, pk=pk)  # Securely fetch book or return 404
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)  # Bind form to existing instance
        if form.is_valid():
            form.save()  # Save changes to the book instance
            return redirect('book_list')  # Redirect to the book list view
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_edit.html', {'form': form, 'book': book})


# View to delete a book
@permission_required('app_name.can_delete', raise_exception=True)
def book_delete(request, pk):
    """
    Handles book deletion. Requires 'can_delete' permission.
    """
    book = get_object_or_404(Book, pk=pk)  # Securely fetch book or return 404
    if request.method == 'POST':
        book.delete()  # Securely delete the book
        return redirect('book_list')  # Redirect to the book list view
    return render(request, 'books/book_confirm_delete.html', {'book': book})