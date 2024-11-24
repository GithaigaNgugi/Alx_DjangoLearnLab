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
