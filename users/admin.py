from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdminConfig(UserAdmin):
    """
    CUSTOM ADMIN INTERFACE
    ORDER ITEMS BY RECENT START DATE
    AND SHOWS EMAIL, USERNAME AND STATUS
    """
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'is_active', 'is_staff')

admin.site.register(User, UserAdminConfig)