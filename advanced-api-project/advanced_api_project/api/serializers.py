from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for the Book model
# This serializer handles all fields of the Book model, including validation.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']  # Specifies fields to serialize

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            # Raise a validation error if the year is in the future
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for the Author model
# This serializer handles the author's name and their related books using nested serialization.
class AuthorSerializer(serializers.ModelSerializer):
    # The books field uses nested serialization to include all related books dynamically
    books = BookSerializer(many=True, read_only=True, source='books')

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  # Specifies fields to serialize

    """
    Relationship Handling:
    - The `books` field dynamically includes all books related to an author.
    - The `related_name="books"` in the Book model's ForeignKey allows reverse lookup.
    - This nested structure enables retrieving all books for an author in a single API response.
    """
