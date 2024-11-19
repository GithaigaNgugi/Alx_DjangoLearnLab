from django.contrib import admin
from .models import UserProfile
from relationship_app.models import UserProfile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
admin.site.register(UserProfile)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'profile_photo', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'date_of_birth']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('email',)

# Register the custom user model in the admin interface
admin.site.register(CustomUser, CustomUserAdmin)
