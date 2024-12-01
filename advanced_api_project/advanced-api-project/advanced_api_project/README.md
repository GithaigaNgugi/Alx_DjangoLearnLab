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
