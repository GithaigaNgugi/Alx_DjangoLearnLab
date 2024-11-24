# Permissions and Groups Setup

## Custom Permissions
The following permissions are defined in the `Book` model:
- `can_view`: Allows viewing book instances.
- `can_create`: Allows creating new book instances.
- `can_edit`: Allows editing book instances.
- `can_delete`: Allows deleting book instances.

## User Groups
- **Viewers**: Can view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Can view, create, edit, and delete books.

## Implementation
- Permissions are enforced using the `@permission_required` decorator in views.
- Groups and permissions can be managed via the Django admin panel.

## Testing
1. Assign users to groups.
2. Log in as these users and verify access to views.
3. Confirm that permissions are enforced as expected.

# Security Measures Implemented

## Settings
- `DEBUG`: Disabled in production for enhanced security.
- `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE`: Cookies are sent only over HTTPS.
- `X_FRAME_OPTIONS`: Prevents clickjacking by disallowing embedding in iframes.
- `SECURE_BROWSER_XSS_FILTER`: Protects against cross-site scripting (XSS) attacks.

## Views
- All input validation is handled via Django forms.
- ORM is used exclusively for database queries to prevent SQL injection.

## Templates
- CSRF tokens are included in all forms to prevent CSRF attacks.
