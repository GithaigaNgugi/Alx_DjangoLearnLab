from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Test suite for Book model API endpoints.
    """

    def setUp(self):
        """
        Create initial test data.
        """
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2023,
            author=self.author
        )
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])

    def test_list_books(self):
        """
        Ensure the list endpoint retrieves all books.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", str(response.data))

    def test_retrieve_book(self):
        """
        Ensure the detail endpoint retrieves a specific book.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_create_book(self):
        """
        Ensure a new book can be created.
        """
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_update_book(self):
        """
        Ensure an existing book can be updated.
        """
        data = {
            "title": "Updated Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """
        Ensure a book can be deleted.
        """
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """
        Ensure books can be filtered by title.
        """
        response = self.client.get(self.list_url, {"title": "Test Book"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_search_books(self):
        """
        Ensure books can be searched by title or author.
        """
        response = self.client.get(self.list_url, {"search": "Test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_order_books(self):
        """
        Ensure books can be ordered by publication year.
        """
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Test Book")
