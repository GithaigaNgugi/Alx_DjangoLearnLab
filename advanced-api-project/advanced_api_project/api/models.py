from django.db import models

# The Author model represents authors in the system.
# Each author can be associated with multiple books.
class Author(models.Model):
    name = models.CharField(max_length=255)  # The name of the author

    def __str__(self):
        return self.name  # Returns the author's name as the string representation


# The Book model represents books in the system.
# Each book is linked to one author using a ForeignKey.
class Book(models.Model):
    title = models.CharField(max_length=255)  # The title of the book
    publication_year = models.IntegerField()  # The year the book was published
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,  # Deletes related books if the author is deleted
        related_name="books"  # Enables reverse relationship lookup as author.books.all()
    )

    def __str__(self):
        return self.title  # Returns the book's title as the string representation
