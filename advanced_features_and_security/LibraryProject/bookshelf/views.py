from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from django import forms

# Create your views here.
@permission_required('app_name.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@permission_required('app_name.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        # Logic for creating a book instance
        pass
    return render(request, 'books/book_create.html')

@permission_required('app_name.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Logic for editing the book instance
        pass
    return render(request, 'books/book_edit.html', {'book': book})

@permission_required('app_name.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        # Redirect to book list or success page
    return render(request, 'books/book_confirm_delete.html', {'book': book})

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)

def secure_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the valid input
            name = form.cleaned_data['name']
