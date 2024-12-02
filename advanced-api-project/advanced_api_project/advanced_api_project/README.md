# Advanced API Project

## API Endpoints

| Endpoint                | HTTP Method | Description                     | Permissions       |
|-------------------------|-------------|---------------------------------|-------------------|
| `/api/books/`           | GET         | Retrieve all books             | Public            |
| `/api/books/<int:pk>/`  | GET         | Retrieve a single book         | Public            |
| `/api/books/create/`    | POST        | Create a new book              | Authenticated     |
| `/api/books/<int:pk>/update/` | PUT   | Update an existing book        | Authenticated     |
| `/api/books/<int:pk>/delete/` | DELETE| Delete a book                  | Authenticated     |

### Key Features
- Utilizes Django REST Framework’s generic views for CRUD operations.
- Implements custom permissions to restrict sensitive actions.
- Easy to extend and customize for additional functionalities.
## Advanced Query Capabilities for Books API

### Features

1. **Filtering**
   Filter books by title, author name, or publication year:
   - `?title=<title>`: Filter by exact title.
   - `?author__name=<author_name>`: Filter by author name.
   - `?publication_year=<year>`: Filter by publication year.

   Example:  

2. **Searching**
Perform text searches on the title or author’s name:
- `?search=<query>`: Search for books.

Example:  

3. **Ordering**
Sort books by any field, such as title or publication year:
- `?ordering=<field>`: Sort in ascending order.
- `?ordering=-<field>`: Sort in descending order.

Example:  

### Default Behavior
- Default ordering: Books are ordered by title in ascending order.
